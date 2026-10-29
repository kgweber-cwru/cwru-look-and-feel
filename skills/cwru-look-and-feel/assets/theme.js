// CWRU colors for Tailwind's CDN build. Load straight after the Tailwind script.
//
// Only the university palette (https://case.edu/brand/visual-identity/color) and tints
// of it. The same values are CSS variables in cwru-tokens.css; test_brand_colors.py
// checks that the two lists agree and that no template uses Tailwind's own color scales.
// Open Sans is the guide's substitute where Arizona Sans is unavailable.
tailwind.config = {
    theme: {
        extend: {
            // Open Sans: the brand's substitute for Arizona Sans (see styles.css)
            fontFamily: {
                sans: ['"Open Sans"', '"Open Sans Fallback"', 'Arial', 'sans-serif'],
            },
            colors: {
                cwru: {
                    blue: '#003071',        // primary: actions, the identity band, headings
                    dark: '#09143A',        // body text, hover on CWRU Blue, footer
                    force: '#2359EF',       // focus rings, link hover
                    true: '#007AB8',        // the MSA program accent; "working" states
                    light: '#A6D2E6',       // on CWRU Blue only, or as a fill
                    'gray-light': '#D3D3D3',
                    bluegreen: '#377E72',
                    copper: '#D63D1F',
                    orange: '#FF9239',
                    violet: '#692C95',      // tertiary: a unit accent; keep under ~5% of a design
                },
                canvas: '#F2F5F8',          // CWRU Blue at 5% on white
                ink: {
                    DEFAULT: '#09143A',     // CWRU Dark Blue
                    muted: '#4E5671',       // Dark Blue at 72%: secondary text, 7.3:1 on white
                    subtle: '#666D85',      // Dark Blue at 62%: meta and placeholders, 5.1:1
                },
                line: {
                    DEFAULT: '#D3D3D3',     // CWRU Light Gray: dividers
                    strong: '#848A9C',      // Dark Blue at 50%: input borders, 3.4:1
                },
                notice: {
                    DEFAULT: '#EDF6FA',     // CWRU Light Blue at 20%: quiet surfaces, hover
                    hover: '#DBEDF5',       // Light Blue at 40%
                },
                success: {
                    DEFAULT: '#377E72',     // Blue Green; white text on it, 4.8:1
                    tint: '#EBF2F1',
                },
                danger: {
                    DEFAULT: '#D63D1F',     // Copper Red; white text on it, 4.6:1
                    tint: '#FBECE9',
                },
                caution: {
                    DEFAULT: '#FF9239',     // Orange: borders and fills only, never text
                    tint: '#FFF2E7',
                },
            },
        },
    },
};
