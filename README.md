# Pebble Sat

Simple server to calculate the next pass (rise, set and positions during the pass) of satellites for a given observer on earth.

Written for the [pb-sat](https://github.com/sarfata/pbsat) project: A Pebble watchface to track satellites.

This can also be used for other projects but if you are going to make a lot of requests please contact and let me know about it. There seems to be no free APIs for satellite tracking which is why I rolled my own. I am happy to share as long as you do not kill my servers ;)

You can also host it yourself on heroku. This project is designed for that.

## References

 - http://libjoe.blogspot.com/2009/10/where-is-my-satellite-in-python.html
 - http://www.sharebrained.com/2011/10/18/track-the-iss-pyephem/
 - http://brainwagon.org/2009/09/27/how-to-use-python-to-predict-satellite-locations/

## Development on Pebble Sat Server

Python on Heroku doc: https://devcenter.heroku.com/articles/getting-started-with-python

### Working on a local machine

Create a virtualenv env:

    virtualenv venv --distribute

Install the packages

    pip install -r requirements.txt

Activate the virtual env environment

    $ source venv/bin/activate

Start the webserver (option1 - heroku-like)

    $ foreman start

Start the webserver (option2 - automatic reload - debug pages)

    $ python main.py

## License

MIT License

Copyright Thomas Sarlandie 2014

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
