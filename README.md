# hep_make_bib_v3
Making bibs for latex/tex based on [the new version of INSPIRE-HEP](https://inspirehep.net/).

# Introduction
Hello friend, are you still upseting to make bibs for latex/tex documents? Here is an example to introduct we who do high energy physics (HEP) research how to anwesr this question. On the base of the [first version](https://github.com/ElonSteveWang/hep_make_bib) and the [second version](https://github.com/ElonSteveWang/hep_make_bib) of  hep_make_bib, I developed the third edition script for automatically make bibs for latex/tex based on the new version of INSPIRE-HEP. For the users of pervious version scripts, this is a perfect version, bacause it adapted new INSPIRE-HEP and fixed all problems of second version script. 

This Python script inner inserted two methods, urllib and requests modules, for users to choose freely, the default method is used requests module. And the biggest difference from previous versions is direct parsing json file rather than parse webpage file. 

# Instrcution

It's used the same ways as [hep_make_bib](https://github.com/ElonSteveWang/hep_make_bib) and [hep_make_bib_v2](https://github.com/ElonSteveWang/hep_make_bib_v2). Here is an example of how to use it.

```
# cd /some/place 
# python3 make_bib.py
Please input your keyword...
JUNO+PRD+2020
Your are searching:  JUNO+PRD+2020
You got  2  result(s) in the index - 1  page. Total:  2  result(s).


Index.  1 , ---------->title:  Detectability of Collective Neutrino Oscillation Signatures in the Supernova Explosion of a 8.8 $M_\odot$ star


%\cite{Sasaki:2019jny}
\bibitem{Sasaki:2019jny}
H.\ Sasaki,\ T.\ Takiwaki,\ S.\ Kawagoe,\ S.\ Horiuchi,\ K.\ Ishidoshiro,
{\it{Detectability of Collective Neutrino Oscillation Signatures in the Supernova Explosion of a 8.8 $M_\odot$ star}},\ {\color{blue}\href{https://doi.org/10.1103/PhysRevD.101.063027}{Phys.\ Rev.\ D\ \textbf{101}\ (2020)\ 6,\ 063027}},\ {\color{blue}\href{https://arxiv.org/abs/1907.01002}{[arXiv:1907.01002[astro-ph.HE]]}}[\href{https://inspirehep.net/literature/1742362}{\scriptsize IN\normalsize SPIRE}]


Index.  2 , ---------->title:  Constraints on the solar $\Delta m^2$ using Daya Bay and RENO data


%\cite{Seo:2018rrb}
\bibitem{Seo:2018rrb}
S.\ Seo,\ S.\ Parke,
{\it{Constraints on the solar $\Delta m^2$ using Daya Bay and RENO data}},\ {\color{blue}\href{https://doi.org/10.1103/PhysRevD.99.033012}{Phys.\ Rev.\ D\ \textbf{99}\ (2019)\ 3,\ 033012}},\ {\color{blue}\href{https://arxiv.org/abs/1808.09150}{[arXiv:1808.09150[hep-ex]]}}[\href{https://inspirehep.net/literature/1691733}{\scriptsize IN\normalsize SPIRE}]
```

For now, you can copy the corresponding bib into your document. As you may have noticed, the usage of the key words is exactly the same as the inspire-hep. Don't explain much, please see the picture below.![example](https://github.com/ElonSteveWang/hep_make_bib/blob/master/example.png) Three hyperlinks are inserted in the highlighted blue text to the corresponding online journal, arxiv and inspire-hep home pages of the article, respectively.

# License
[hep_make_bib_v3](https://github.com/ElonSteveWang/hep_make_bib_v3) is available under the [GNU General Public License, version 2](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

This project can also be used on other websites with a few changes. If someone based on this work for the second development, please indicate the source, thank you!
