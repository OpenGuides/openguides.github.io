#!/usr/bin/perl -w

use strict;

use CGI;
use Template;

my $q = CGI->new();

my $template = Template->new({
        INCLUDE_PATH => '/home/earle/openguides.org/talks/yapc-eu-2003/templates/',
});

# Initialise variables.

my $vars = {};

# Get what page we're looking at from the CGI parameter "page".

my $page = $q->param('page') || '';

print "Content-Type: text/html\n\n";

# Eval for catching TT errors.

eval {

 	# If a page was specified, put it in the template variable 'page'.

	if ($page) {
		$vars = {
			page => $page
		};

	}

	# If no page was specified, use the default page "contents".

	else {

		$vars = {
			page => 'contents'
		};
	}

	# Process the wrapper template with the page variable.

	$template->process('wrapper', $vars);

}; 

# If TT threw an error:

if ($template->error()) {
	
	# Put the TT error message into a template variable.

	$vars = { error => $template->error };

	# Process a special error template with the error variable.

	$template->process('error',$vars);

};
