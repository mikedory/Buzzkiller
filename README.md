##Buzzkiller##

__Wait, what?__

So I can't speak for you, but I don't like buzzwords.  I've worked in media companies and the tech startup scene long enough to start to actually get a little itchy when someone starts tossing them out.  Of course, I'm not all that much better — I've certainly seen a bunch fall out of my mouth too, and that makes me sadder yet.

A while back, I'd read about [Matt Might](matt.might.net)'s [weasel word Perl scripts](http://matt.might.net/articles/shell-scripts--fileor-passive-voice-weasel-words-duplicates/), and I loved the idea.  So, after a conversation with some friends about buzzword-crazed emails, I decided I wanted to port the idea to Python.

This is so very, __very__ much a work in progress, but so far, it's fun!

Usage is pretty straightforward: the script will run a check against the files stored, and it will tell you all about the things it finds.  It's looking for buzzwords, office jargon-type terms, and weasel words (as defined by Matt as noted above).


You would run it thusly:

	./buzzkiller.py many various peak performance top-down silo

To use a file full of words to check against, instead of the command line, try it this way:

	./buzzkiller.py --file exampleFile.txt

To run it with a file and extra arguments, you might do that like this:

	./buzzkiller.py --file exampleFile.txt many various peak performance top-down silo

You can also specify an output file, like so:

	./buzzkiller.py --log 'output.txt'

There's also a verbose mode, in case you were curious as to what was being searched for and against:

	./buzzkiller.py --file exampleFile.txt -v

To do everything, try this:

	./buzzkiller.py --file exampleFile.txt -v --log 'output.txt' many various peak performance top-down silo

And depending on what you're searching, you'll probably see output like this:

	Here goes some parse magic...

	checking file named weaselwords.txt
	checking file named buzzwords.txt
	checking file named officewords.txt

	Alrighty, let's see what you've got here: 

	WEASELWORD: many
	WEASELWORD: few
	OFFICEWORD: bandwidth
	OFFICEWORD: orbit
	BUZZWORD: cloud



Oh also, you'll need the [argparse](http://docs.python.org/dev/library/argparse.html) module for Python.  If you're running Python 2.7+, you should already have it.  If not, you should be able to install it with easy_install or apt-get or whatever works on the system you're using.

Finally, I should note, the list of buzzwords is cobbled together from a few internet sources discussing the matter, most notably [this post](http://www.adamsherk.com/public-relations/most-overused-press-release-buzzwords/) from [Adam Sherk's blog post on the subject](http://www.adamsherk.com/) and [Marlys Harris' column on office terms](http://moneywatch.bnet.com/saving-money/blog/consumer-reporter/words-you-should-never-use-at-the-office-unless-you-have-to/292/?tag=col1;blog-river).  More will be added, and attributed, accordingly.

P.S. I should note that doing any of this would have been way giant amounts harder (and probably never attempted) were it not for [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/documentation.html) and [Adam Parrish](http://decontextualize.net)'s awesome [Python tips](http://itpedia.nyu.edu/wiki/Introduction_to_Python).