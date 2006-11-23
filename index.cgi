#!/usr/bin/perl

use warnings;
use strict;

my $url = "http://openguides.org/";
my $env = '';

if ($ENV{'QUERY_STRING'}) {
  $env = $ENV{'QUERY_STRING'};
  $env =~ s/page=//;
  $env = 'page/' . $env;
}

print <<HTML;
Server Response: http://openguides.org/index.cgi
Status: HTTP/1.1 301 Moved Permanently
Content-Type: text/html
Location: $url$env

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<meta http-equiv="Refresh" content="0; url=$url$env">
	<meta http-equiv="Status" content="HTTP/1.1 301 Moved Permanently">
	<meta http-equiv="Location" content="$url$env">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>301 Moved Permanently</title>
</head>
<body>
<h1>301 Moved Permanently</h1>
<p>
This resource has moved to <a href="$url$env">$url$env</a>.
</p>
</body>
</html>
HTML
