#!/usr/bin/perl

use warnings;
use strict;

use CGI;
use Template;

my $q        = CGI->new;
my $template = Template->new({ INCLUDE_PATH => 'templates' });
my $page     = $q->param('page') || '';

print "Content-Type: text/html\n\n";

eval
{
  # If a page was specified, put it in the template variable 'page'.
  # If no page was specified, use the default page "contents".
  my $selected_page = 'contents';

  $selected_page = $page if $page;

  my $vars = { page => $selected_page };

  # Process the wrapper template with the page variable.
  $template->process('wrapper', $vars);
}; 

if ($template->error)
{  
  my $vars = { error => $template->error };
  $template->process('error', $vars);
};