#!/usr/bin/perl
use CGI;

$CGI = new CGI;

$CGI::POST_MAX = 1024;  # max 1K posts
$CGI::DISABLE_UPLOADS = 1;  # no uploads

#print $CGI->header;
#print $CGI->start_html('Results');

# "mstu12", "ecs28", "cont80"

if ($CGI->param())
{
	# bd,wd,bc,wc
	$designs  = $CGI->param("BD");
	$designs .= ',' . $CGI->param("WD");
	$designs .= ',' . $CGI->param("BC");
	$designs .= ',' . $CGI->param("WC");

	$seen = $CGI->param("seen");
	$year = $CGI->param("year");

	$group = $CGI->param("group");

	%groupnames = ("mstu12",  "maths",
		           "ecs28",   "childhood",
		           "cont80",  "control",
		           "test",    "testing");

	$capsgroup = $groupnames{$group};
	$capsgroup =~ tr/a-z/A-Z/;  # convert to upper case

	$file = "../data/" . $groupnames{$group} . ".txt";

	$ip = $CGI->remote_host();
	($second, $minute, $hour, $dayOfMonth, $month, $yearOffset, $dayOfWeek, $dayOfYear, $daylightSavings) = gmtime();
	$dateyear = 1900 + $yearOffset;
	$month += 1;
	$date = "$hour:$minute:$second $dayOfMonth/$month/$dateyear";

	open(FILE, ">> $file") || print("can't open file: $!");
	print FILE $capsgroup . ',' . $ip . ',' . $date . ',';
	print FILE $designs, ',', $seen, ',', $year, "\n";
	close(FILE);
}

#print $CGI->end_html;

print $CGI->redirect("http://www.mjisite.streamlinenettrial.co.uk/thankyou.html");
