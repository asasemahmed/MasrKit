#!/usr/bin/env node

import { cpSync, existsSync, mkdirSync, readdirSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const skillsRoot = join(root, "skills");

const targets = {
  codex: join(process.env.CODEX_HOME || join(homedir(), ".codex"), "skills"),
  claude: join(homedir(), ".claude", "skills"),
  cursor: join(homedir(), ".cursor", "skills"),
  gemini: join(homedir(), ".gemini", "skills"),
};

const help = `MasrKit skill installer

Usage:
  masrkit --all (--target <agent> | --dest <path>) [--dry-run]
  masrkit --skill <name> [--skill <name> ...] (--target <agent> | --dest <path>) [--dry-run]
  masrkit --list

Options:
  --all              Install every skill
  --skill <name>     Install one skill; repeatable
  --target <agent>   codex, claude, cursor, or gemini
  --dest <path>      Custom skills directory
  --dry-run          Show changes without writing files
  --list             List available skills
  --help             Show this help
`;

function availableSkills() {
  return readdirSync(skillsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && existsSync(join(skillsRoot, entry.name, "SKILL.md")))
    .map((entry) => entry.name)
    .sort();
}

function fail(message) {
  console.error(`Error: ${message}`);
  process.exitCode = 2;
}

function parseArgs(argv) {
  const options = { all: false, skills: [], dryRun: false };

  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--all") options.all = true;
    else if (argument === "--dry-run") options.dryRun = true;
    else if (argument === "--list") options.list = true;
    else if (argument === "--help" || argument === "-h") options.help = true;
    else if (["--skill", "--target", "--dest"].includes(argument)) {
      const value = argv[index + 1];
      if (!value || value.startsWith("--")) throw new Error(`${argument} requires a value`);
      index += 1;
      if (argument === "--skill") options.skills.push(value);
      if (argument === "--target") options.target = value;
      if (argument === "--dest") options.dest = value;
    } else {
      throw new Error(`Unknown option: ${argument}`);
    }
  }

  return options;
}

function validateOptions(options, available) {
  if (options.help || options.list) return;
  if (options.all === (options.skills.length > 0)) {
    throw new Error("Choose exactly one of --all or --skill");
  }
  if (Boolean(options.target) === Boolean(options.dest)) {
    throw new Error("Choose exactly one of --target or --dest");
  }
  if (options.target && !Object.hasOwn(targets, options.target)) {
    throw new Error(`Unknown target: ${options.target}`);
  }
  for (const skill of options.skills) {
    if (!available.includes(skill)) throw new Error(`Unknown skill: ${skill}`);
  }
}

function install(names, destination, dryRun) {
  for (const name of names) {
    const source = join(skillsRoot, name);
    const target = join(destination, name);
    if (existsSync(target)) throw new Error(`Refusing to overwrite existing path: ${target}`);
    console.log(`${dryRun ? "Would install" : "Installed"} ${name} -> ${target}`);
    if (!dryRun) {
      mkdirSync(destination, { recursive: true });
      cpSync(source, target, { recursive: true, errorOnExist: true });
    }
  }
}

try {
  const options = parseArgs(process.argv.slice(2));
  const available = availableSkills();
  validateOptions(options, available);

  if (options.help) {
    console.log(help);
  } else if (options.list) {
    console.log(available.join("\n"));
  } else {
    const names = options.all ? available : [...new Set(options.skills)];
    const destination = resolve(options.dest || targets[options.target]);
    install(names, destination, options.dryRun);
  }
} catch (error) {
  fail(error instanceof Error ? error.message : String(error));
}
