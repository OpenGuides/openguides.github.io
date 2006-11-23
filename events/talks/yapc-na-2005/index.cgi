#!/usr/bin/perl

use warnings;
use strict;

use CGI 'param';
use Template;

run();

sub run
{
 my $template = Template->new({
                                EVAL_PERL    => 1,
                                INCLUDE_PATH => 'templates'
                              });
 my $vars     = {};
 my $page     = CGI->new->param('keywords') || '';

 print "Content-Type: text/html\n\n";

 # Eval for catching TT errors.

 eval
 {
   if ($page) { $vars = { page => $page };      }
   else       { $vars = { page => 'contents' }; }

   $template->process('wrapper', $vars);
 }; 


 error($template->error) if $template->error;
}

sub error
{
  my $error = shift || "No error given, something went wrong!";

  print <<HTMLSTOP;
<html>
<head>
<title>Error</title>
</head>
<body>
<h1>Error</h1>
<h2>$error</h2>
</body>
</html>
HTMLSTOP

};
