# Patterns

Markup that put the rules together in an internal CWRU web application (Tailwind CDN plus a small stylesheet; the ideas hold in any stack). Adapt, do not paste blindly.

## Header with unit accent

```html
<header class="bg-cwru-blue text-white border-b-4 border-[color:var(--unit-accent)]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between gap-4">
    <div class="flex items-center min-w-0">
      <a href="/" class="block flex-shrink-0">
        <!-- supplied reversed logo; the file already includes the clear space -->
        <img src="/static/images/cwru-two-line-logo-white-clearspace.webp"
             alt="Case Western Reserve University" width="470" height="88" class="h-[54px] w-auto">
      </a>
      <p class="hidden md:block border-l border-cwru-light/50 ml-1 pl-5 leading-snug">
        <span class="block font-semibold">Product name</span>
        <span class="block text-sm text-cwru-light">Unit name</span>
      </p>
    </div>
    <nav><!-- white links; hover bg-cwru-dark; focus outline Light Blue --></nav>
  </div>
</header>
```

At 54px tall that logo is 261 x 27: just over the 255 x 25 minimum. Never shrink it for a phone; let the product name hide instead, as above.

## Footer

```html
<footer class="bg-cwru-dark">
  <div class="max-w-7xl mx-auto px-4 py-4 text-center text-sm text-cwru-gray-light">
    Product name | Case Western Reserve University
  </div>
</footer>
```

## Buttons and focus

- Primary: `bg-cwru-blue text-white`, hover `bg-cwru-dark`. Secondary: white with a CWRU Blue border and text, hover the `notice` tint.
- Destructive: `bg-danger text-white` (Copper Red, 4.62:1).
- Focus: `outline: 2px solid var(--cwru-force); outline-offset: 2px`. Inside the blue header use Light Blue, because Force Blue on CWRU Blue is nearly invisible.
- Touch targets 48px tall on phones; disable a button while its request is in flight when running twice is harmful.

## Browser-drawn surfaces

Theme the parts the browser draws so nothing off-palette leaks through: `accent-color` (checkboxes, radios), `caret-color`, `::selection` (Light Blue background, Dark Blue text), `::placeholder` (ink-subtle), `scrollbar-color`. Included in `assets/cwru-tokens.css`.

## Status messages

| Meaning | Surface | Text | Border/accent | Also |
|---|---|---|---|---|
| Success | success-tint | Dark Blue | Blue Green | check icon |
| Error | danger-tint | Dark Blue | Copper Red | warning icon, plain next step |
| Caution | caution-tint | Dark Blue | Orange | warning icon |
| Info | notice | Dark Blue | True Blue | info icon |

Dark Blue text on tints keeps contrast high; the color lives in the border and icon. Orange is never text.

## Errors in CWRU voice

Say what failed, why when known, and what to do. Never show an exception's text.

- Not: "An error occurred while processing your request."
- Yes: "Your answer wasn't sent. It's still in the box. Try again."
- Not: "Unauthorized access."
- Yes: "Your sign-in timed out. Sign in again to continue."

## Letting the palette be enforced

Keep the allow-list test in CI. When someone needs a new color, the conversation goes: can an existing role do it? Is it a tint of a palette color (add with source and percentage)? Otherwise it is a question for brand@case.edu, not a code change.
