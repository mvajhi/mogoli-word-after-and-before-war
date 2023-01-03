from wordcloud_fa import WordCloudFa

wodcloud = WordCloudFa(no_reshape=True, persian_normalize=True, include_numbers=False, collocations=False, width=1600, height=800, background_color="white")
text = ""
with open('book.txt', 'r') as file:
    text = file.read()
wc = wodcloud.generate(text)
image = wc.to_image()
image.show()
image.save('output.png')