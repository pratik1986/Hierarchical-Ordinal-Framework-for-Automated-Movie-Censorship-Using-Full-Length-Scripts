:: =============================================================================
:: Script: search_queries.bat
::
:: Description:
::     Opens Google search queries for a predefined list of movie titles to
::     facilitate retrieval of publicly available screenplay files from
::     scripts.com during dataset construction.
::
:: Purpose:
::     During development of the movie script dataset used in the paper
::     "Hierarchical Ordinal Framework for Automated Movie Censorship Using
::     Full-Length Scripts" (IEEE GCAT 2025), screenplay files were collected
::     from publicly accessible online sources. This utility automates the
::     generation of search queries, reducing the manual effort required to
::     locate individual scripts.
::
:: Functionality:
::     - Opens one browser tab per movie title.
::     - Searches Google using:
::           "<movie title> script site:scripts.com"
::     - Assists the manual dataset acquisition process.
::
:: Inputs:
::     - List of movie titles.
::
:: Outputs:
::     - Google search pages for screenplay retrieval.
::
:: Author:
::     Pratik N. Kalamkar
:: =============================================================================


@echo off
start https://www.google.com/search?q=Last+Tango+in+Paris+script+site:scripts.com
start https://www.google.com/search?q=Pink+Flamingos+script+site:scripts.com
start https://www.google.com/search?q=The+Big+Feast+script+site:scripts.com
start https://www.google.com/search?q=The+Story+of+O+script+site:scripts.com
start https://www.google.com/search?q=The+Evil+Dead+script+site:scripts.com
start https://www.google.com/search?q=Santa+Sangre+script+site:scripts.com
start https://www.google.com/search?q=Henry+%26+June+script+site:scripts.com
start https://www.google.com/search?q=Whore+script+site:scripts.com
start https://www.google.com/search?q=Man+Bites+Dog+script+site:scripts.com
start https://www.google.com/search?q=Kids+script+site:scripts.com
start https://www.google.com/search?q=Showgirls+script+site:scripts.com
start https://www.google.com/search?q=Crash+script+site:scripts.com
start https://www.google.com/search?q=Orgazmo+script+site:scripts.com
start https://www.google.com/search?q=Happiness+script+site:scripts.com
start https://www.google.com/search?q=The+Dreamers+script+site:scripts.com
start https://www.google.com/search?q=Young+Adam+script+site:scripts.com
start https://www.google.com/search?q=A+Dirty+Shame+script+site:scripts.com
start https://www.google.com/search?q=Ma+mere+script+site:scripts.com
start https://www.google.com/search?q=Lust%2C+Caution+script+site:scripts.com
start https://www.google.com/search?q=Frontier(s)+script+site:scripts.com
start https://www.google.com/search?q=A+Serbian+Film+script+site:scripts.com
start https://www.google.com/search?q=Shame+script+site:scripts.com
start https://www.google.com/search?q=Elles+script+site:scripts.com
start https://www.google.com/search?q=Blue+Is+the+Warmest+Colour+script+site:scripts.com
start https://www.google.com/search?q=Blonde+script+site:scripts.com
