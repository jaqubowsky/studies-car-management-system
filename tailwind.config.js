/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html', './static/src/**/*.js'],
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 5s forwards',
      },
      keyframes: {
        fadeIn: {
          '0%, 90%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};
