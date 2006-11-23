#!/usr/bin/perl

use warnings;
use strict;

use CGI;
use Template;

my $cgi = CGI->new;

my $tt = Template->new({
		INCLUDE_PATH => 'templates',
		PRE_PROCESS  => 'config:header',
		POST_PROCESS => 'footer',
		PRE_CHOMP    => 1,
		POST_CHOMP   => 1
	});

print "Content-Type: text/html\n\n";

my $page = $cgi->param('page') || 'home';
my $vars = { page => $page };

$tt->process($page, $vars) || error($tt->error);

sub error {
	my $error = shift;

	print <<HTML;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<title>Error</title>
<style type="text/css">
body {
	background: #fff;
	color: #000;
	margin: 10px;
	font: 1em Verdana, Arial, sans-serif
}
blockquote {
	background: #ccc;
	color: #000;
	border: 1px dotted #000;
	padding: 10px
}
</style>
</head>
<body>
<h1>Error</h1>
<p>
Something has gone wrong. Here's what Template Toolkit had to say:
</p>
<blockquote>
$error()
</blockquote>
</body>
</html>
HTML

}
