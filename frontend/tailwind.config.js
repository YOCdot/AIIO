/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
    container: {
      center: true,
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    // daisyUI config (optional)
    styled: true,
    // themes: true,
    themes: [
        {
            mytheme: {
                "primary": "#570DF8",
                "secondary": "#F000B8",
                "accent": "#37CDBE",
                "neutral": "#3D4451",
                "base-100": "#FFFFFF",
                "info": "#3ABFF8",
                "success": "#36D399",
                "warning": "#FBBD23",
                "error": "#F87272",
            },
        },
    ],
    base: true,
    utils: true,
    logs: true,
    rtl: false,
    prefix: "",
    darkTheme: "dark",
  },
};
