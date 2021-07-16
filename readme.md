# Simplette CSS Stylesheet

Simplette is a relatively basic CSS stylesheet whose main purpose is to provide a simple and yet functionnal set of styles that make it easier to generate webpages with a consistent appearance.

One of the main "advantages" is the fact that there is no hidden margins paddings or spacings, you have to manually toggle/enable them when and where you want them.<br>
This might seem a bit cumbersome, but it makes it easier to generate a web page with a consistent appearance without having to fight the stylesheet itself.<br>
And whatever spacing you chose to enable will always be the same value: 1em (Expect for the 2 classes)</p>

## Stylesheets

### css/simplette.base.min.css
Contains the base of the stylesheet with the following features:<br>
&nbsp;&nbsp;● Text & headings<br>
&nbsp;&nbsp;● Containers (Margins only)<br>
&nbsp;&nbsp;● Lists<br>
&nbsp;&nbsp;● Details<br>
&nbsp;&nbsp;● Forms

And through the [config file](scss/abstract/options.scss), you can include the content of the other stylesheets.

### css/simplette.grid.min.css
Contains the grid system.

### css/simplette.fancy.min.css
Contains a couple of fancy styles to lighten up you page:<br>
&nbsp;&nbsp;● Containers borders<br>
&nbsp;&nbsp;● Gradients<br>
&nbsp;&nbsp;● Frames

### css/simplette.all.min.css
Contains everything in a single file.

## Building

Firstly, you have to make sure you have the required Python modules installed, or install them using this command:<br>
`pip install --upgrade -r requirements.txt`

Afterward, you can simply run `compile.py` or `compile.bat` and let the magic happen.

## Configuring

Simplette can be configured by changing some of the options in the "*[scss/abstract/options.scss](scss/abstract/options.scss)*" file.

For more info on each of the option, please refer to the file in question.

## Elements & Classes

All of the classes and their effect are documented on the [demo page](https://aziascreations.github.io/Simplette-CSS-Stylesheet/).

## License

[Unlicense](LICENSE)
