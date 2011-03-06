##Buzzkiller##

__Wait, what?__

So I can't speak for you, but I don't like buzzwords.  I've worked in media companies and tech startups long enough to start to actually get a little itchy when someone says one.  Of course, this generally means a bunch fall out of my mouth too, and that makes me sadder.

A while back, I'd read about [Matt Might](matt.might.net)'s [weasel word Perl scripts](http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/), and I loved the idea.  So, after a conversation with a friend about buzzword-crazed emails, I decided I wanted to port the idea to Python.

This is so very, __very__ much a work in progress, but so far, it's fun!

Usage is pretty straightforward: the script will run a check against the files stored, and it will tell you all about the things it finds.


You would run it thusly:

	./buzzkiller.py many various peak performance top-down silo

To use a file full of words to check against, instead of the command line, try it this way:

	./buzzkiller.py -f exampleFile.txt

To run it with a file and extra arguments, you might do that like this:

	./buzzkiller.py -f exampleFile.txt many various peak performance top-down silo

You can also specify an output file, like so:

	./buzzkiller.py --log 'output.txt'

There's also a verbose mode, in case you were curious as to what was being searched for and against:

	./buzzkiller.py -f exampleFile.txt -v

To do everything, try this:

	./buzzkiller.py -f exampleFile.txt -v --log 'output.txt' many various peak performance top-down silo


Oh also, you'll need the [argparse](http://docs.python.org/dev/library/argparse.html) module for Python.  If you're running Python 2.7+, you should already have it.  If not, you should be able to install it with easy_install or apt-get or whatever works on the system you're using.