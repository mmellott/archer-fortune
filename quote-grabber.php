<?php


`wget -O /tmp/page "http://www.tvfanatic.com/quotes/shows/archer/"`;

libxml_use_internal_errors(true);

$page = DOMDocument::loadHTMLFile('/tmp/page');
$paragraphs = $page->getElementsByTagName('p');

foreach( $paragraphs as $p ){
	if( stripos( $p->getNodePath(), 'blockquote') ){
		foreach ($p->childNodes as $pChild) {
			if ($pChild->nodeType === XML_TEXT_NODE) {
				file_put_contents('archer', trim($pChild->textContent)."\n", FILE_APPEND);;
			}
		}
		file_put_contents('archer',"%\n", FILE_APPEND);
	}
}

for( $i = 2; $i < 62; $i++ ){

	sleep(1);

	`wget -O /tmp/page "http://www.tvfanatic.com/quotes/shows/archer/page-$i.html"`;

	libxml_use_internal_errors(true);

	$page = DOMDocument::loadHTMLFile('/tmp/page');
	$paragraphs = $page->getElementsByTagName('p');

	foreach( $paragraphs as $p ){
		if( stripos( $p->getNodePath(), 'blockquote') ){
			foreach ($p->childNodes as $pChild) {
				if ($pChild->nodeType === XML_TEXT_NODE) {
					file_put_contents('archer', trim($pChild->textContent)."\n", FILE_APPEND);;
				}
			}
			file_put_contents('archer',"%\n", FILE_APPEND);
		}
	}
}
