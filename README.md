# webapp_builder

Build a website element by element by typing in natural language.

Used nltk for tagging texts and bootstrap elements for generating layouts.

Example prompts:
<section (header, body, footer)> <function> <content>
1. `Hi, give me a header with the title 'Culinary Chronicles' and the description as 'A journey through global flavours, recipes, and culinary traditions.'`
2. `To the body add the description 'description for the body'`
3. `To the footer add the title 'Acknowledgments'`
4. `to the body add the image 'hero_image.png/300x200'` or `to the body add the image 'hero_image.png'` (default: 500x500)
5. `to the body add the table 'sample_csv.csv'`
6. To restart: `clear`
7. To save progress: `save` Then refresh
