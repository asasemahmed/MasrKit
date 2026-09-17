# RTL browser test matrix

Run the matrix at a narrow phone width, a wider phone width, and desktop:

1. Load directly into RTL and switch from LTR to RTL without reload if supported.
2. Tab from browser chrome through the page; compare focus order with reading order.
3. Open dialogs, selects, date pickers, tooltips, toasts, and menus rendered in portals.
4. Enter Arabic, Latin, digits, `+20`, punctuation, email, and a long URL.
5. Select, copy, paste, delete, and move the caret inside mixed-direction input.
6. Inspect overflow: tables, code, charts, carousels, sticky edges, and shadows.
7. Test zoom/text enlargement and landscape orientation.
8. Check back/next, chevrons, brand marks, media controls, and status icons.
9. Verify print/PDF output if it is a supported product path.
10. Repeat in supported Chromium, Firefox, and WebKit engines; record browser-specific evidence.
