# webapp_builder

A website development tool that is unconventional from other generative AI website builders as it allows users to build
website components sequentially and customise each component as per their choice.

I have used nltk for tokenization and pyweb.io for generating the UI components. Pyweb.io can be replaced with any frontend templates of your choice.

Some example prompts are:

\<section (header, body, footer)\> \<function\> '\<content\>'
1. `Hi, give me a header with the title 'Culinary Chronicles' and the description as 'A journey through global flavours, recipes, and culinary traditions.'`
2. `To the body add the description 'description for the body'`
3. `To the footer add the title 'Acknowledgments'`
4. `to the body add the image 'hero_image.png/300x200'` or `to the body add the image 'hero_image.png'` (default: 500x500)
5. `to the body add the table 'sample_csv.csv'`
6. `To the body add the text 'content for the body'`
7. To restart: `clear`
8. To save progress: `save` Then refresh

Current features: heading, subheading, body text, images, tables, clear, save.
