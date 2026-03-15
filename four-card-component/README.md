# Frontend Mentor - Four card feature section solution

This is a solution to the [Four card feature section challenge on Frontend Mentor](https://www.frontendmentor.io/challenges/four-card-feature-section-weK1eFYK). Frontend Mentor challenges help you improve your coding skills by building realistic projects. 

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
  - [AI Collaboration](#ai-collaboration)
- [Author](#author)

**Note: Delete this note and update the table of contents based on what sections you keep.**

## Overview

### The challenge

Users should be able to:

- View the optimal layout for the site depending on their device's screen size

### Screenshot
![](./images/screenshots.jpg)

### Links

- Solution URL: [GitHub](https://github.com/MasoNord/Tiny-Project-Collection/tree/main/four-card-component)
- Live Site URL: [Vercel](https://four-card-components-chi.vercel.app/)

## My process

### Built with

- Semantic HTML5 markup
- CSS custom properties
- Flexbox
- CSS Grid
- Mobile-first workflow


### What I learned

In this project I learned how to use flexbox and grid css layouts together. The most interesting part for me was usage of grid-template-area in practice. I understand how to use this css property in order to place cards the same as on design mockup

The following css code draw the structure of a grid area

```css
    .cards {
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, 1fr);
        grid-template-areas: 
        "start mid1 end"
        "start mid2 end";       
    }
```

Each grid sub area is applied to specific card

```css
    .supervisor  {
        grid-area: start;
        align-self: center;
    }

    .teambuilder {
        grid-area: mid1;
    }

    .karma {
        grid-area: mid2;
    }
    .calculator {
        grid-area: end;
        align-self: center;
    }
```

### Useful resources

- [Box shadows guide](https://css-tricks.com/almanac/properties/b/box-shadow/) - This helped me to drow shadows for the cards
- [Transaction property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition) - This helped me to understand how to make simple animation in CSS
- [CSS Grid Layout Guide](https://css-tricks.com/complete-guide-css-grid-layout/)

**Note: Delete this note and replace the list above with resources that helped you during the challenge. These could come in handy for anyone viewing your solution or for yourself when you look back on this project in the future.**

### AI Collaboration
- I used ChatGPT to help me understand how to work with grid-template-areas

## Author
- Frontend Mentor - [@MasoNord](https://www.frontendmentor.io/profile/MasoNord)