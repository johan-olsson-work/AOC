test_data = [{"input": "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb", "output": "fdgacbe cefdb cefbgd gcbe"},
             {"input": "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec", "output": "fcgedb cgb dgebacf gc"},
             {"input": "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef", "output": "cg cg fdcagb cbg"},
             {"input": "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega", "output": "efabcd cedba gadfec cb"},
             {"input": "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga", "output": "gecf egdcabf bgf bfgea"},
             {"input": "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf", "output": "gebdcfa ecba ca fadegcb"},
             {"input": "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf", "output": "cefg dcbef fcge gbcadfe"},
             {"input": "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd", "output": "ed bcgafe cdgba cbgef"},
             {"input": "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg", "output": "gbdfcae bgc cg cgb"},
             {"input": "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc", "output": "fgae cfgab fg bagce"}]


input_data = [{"input": "bgeacd dbfag bcadegf agdce dgfbce bgc bdgca aedcgf bc abec", "output": "gcdfbe cbea bc gbc"},
              {"input": "bdeag gdbaec cd dgc abcfg ebcd dgfabe cdfeag cgadb bdagfce", "output": "becd acfgde bgcaed eadgbc"},
              {"input": "acbfg bcf ebacg fb fcbgea cbdfge cgeabd agcfd aebf bdaefgc", "output": "fbcdeg cfb ebgca bf"},
              {"input": "bfcde dfgb gecbdf fdc fdcega fd ebdca gfcaedb gcfbe cbagef", "output": "dbfec gbfd bcdfe dfc"},
              {"input": "dbgeaf bad acdfbe ab agbdf bgcdf fdgae fcgbdea fgecda egab", "output": "ba dab abd gbae"},
              {"input": "feagcb cdfagb egda bdg dg fdcagbe ebcga bedfc bgecd dbcgea", "output": "eafgbc bcdfage dg egad"},
              {"input": "bacfedg afbgc dbcgaf afgecd acd bfagce bgda ad adfbc ecbdf", "output": "dca dca abdg dcbef"},
              {"input": "eagfb efcdba faceg gfdce cea afbcegd ac afdegb gafcbe gbac", "output": "fegcd geafc edbcaf bcag"},
              {"input": "cfb bgfce ebgdf fc gdfeab acdbfeg cgeab ecfd badfcg ebcfgd", "output": "ecgab eagcb efbacdg fc"},
              {"input": "adfec ebdcgf bfced bec fagcdeb gbcd cb fbgde deagbf afecgb", "output": "bce cb fdgeb bc"},
              {"input": "bgfaec dcfga ed acedgfb fdebgc dec fdeb gedcba gfced cebfg", "output": "cde agcbde gfaecb cde"},
              {"input": "bgefc cfgbea dfgaecb dg dbcg dcefa dfbegc dgfce afgedb fgd", "output": "cfged gdf fbgdea gafecb"},
              {"input": "fcbade dagbe gacb gaedfc bdaecfg bgfde dbaec baegcd ga dga", "output": "ag gad gcab ga"},
              {"input": "cfgdeb cbfade fac badfc ca gafdce gfdebac bfadg fbdce aceb", "output": "ebdcf deagfc ac ebfcd"},
              {"input": "debfcg fgde cfaedgb ecbag cbeadf gf gbf fdceb fcebg dfagbc", "output": "gbfec gf agbce bfcagd"},
              {"input": "fdcebag cbeagd gafed dfbgc cgedfa beg be edgafb edbfg eabf", "output": "gbcfd acgefd cfdageb afged"},
              {"input": "bgad efdbcg aecfdgb fgebca ga cgade acbedg adfce aeg cgdeb", "output": "gdecfb fgdceb adceg ga"},
              {"input": "acefd efdb cgabfe be fegcbda gbacd cagefd eab acebfd acbed", "output": "be debf feacgb becad"},
              {"input": "edbcag dgefcab ce fgdcb eafc afgceb gfbae cbe degafb bfgce", "output": "fcgbd ec dbaegc efgdba"},
              {"input": "bfcdge gfcbda aegfcdb dg cdgbe dbfce dgb fged cdefba caebg", "output": "dbg bgd gdfe dg"},
              {"input": "bfeadc dbfcgea bgdaf decfg efdabg cgba fbdagc ca fca gdcfa", "output": "cafdg gacb bdfeag ac"},
              {"input": "edbcfg cdgfae gedaf egcfd beagfc fga bcfdgae cgda debfa ag", "output": "defgc efabgc fcegadb fegda"},
              {"input": "gafcb fcgadb gdca gbadf ad fbegd befcag fda ebgdcaf fbaecd", "output": "agcbf dbafcg dgafb abgfcd"},
              {"input": "cga gafce gecbfda dbacgf defac febcg cfbdeg afegcb bgae ga", "output": "cdbgef ebdagcf caefg geba"},
              {"input": "gfebcda ab dfabg abcfgd gdbfc abgc becgdf bcedfa adfge fab", "output": "abf fab ba agbc"},
              {"input": "fagce ceabfgd cdea cbfaeg dgafce egcdf bfaegd gbcdf fde ed", "output": "de aedgbf fecagd fcebga"},
              {"input": "fcbad fe afge ebagd fde fbdegac fgbced fdgeba fabed edcgba", "output": "debga bdgae bafdc efag"},
              {"input": "adbfg ba dbcfga abgdecf gfedb agfdc gcdeaf adfebc bda bacg", "output": "befdac ebdafc abd gdbafce"},
              {"input": "begfd dgfbac dgbac ce bedgac dafceg dgbce ecfdgab ceg ecab", "output": "gadfcb gefdb gdeafcb fgcdab"},
              {"input": "dcfagbe dgbefa gdbcea faebgc fade efabg dge cfdbg fbgde ed", "output": "de efbacg dfea dfea"},
              {"input": "dcfeag bgefcad dcgfe afedb cb bfgaec dcgb bec fcdbe gbecdf", "output": "bec agfebc ecb edfba"},
              {"input": "acdbgfe ebcag fgc feagcb bafc gfceb fc gfadce gcbead dbgef", "output": "bceagd fcab gfdceba cfebg"},
              {"input": "bdegf abgefd fgba dgceab dabcef badfegc egb fadeb gb fdgce", "output": "gafb efdba gb dbfage"},
              {"input": "bfdca cfgb agdfec caf bgcfda becad gbdaf fc ebgfcad bagedf", "output": "gefdab cebad cf bgfc"},
              {"input": "dfbcge bedgaf bgefd cgebda efcb gcfad degfbca bgc fcdbg cb", "output": "ecbadg gbfdc bgdfe fcbe"},
              {"input": "dfeagc bfacge abfc fcegb bdecg bef acfeg bf bcgaedf gedfba", "output": "bf ebf fb cfadegb"},
              {"input": "fbgdc fcbgead egaf acebgd gacdf fad gdaec bfecad fa gcedaf", "output": "eafdgc fda degacf geadbc"},
              {"input": "fcdea gcdbaf cgedbf bd bgde cdb acfgeb efcbg fdecb fedbacg", "output": "aebgcf febdc dcb bgdefc"},
              {"input": "bfdeg dbcefa bdaegf cegdf agdb fdaeb bge gb beacfg edbcafg", "output": "gefdb edcfg acbgef egb"},
              {"input": "afgedbc caebg gef fbec egcdba dfgabe gafcd bfacge agcfe ef", "output": "fge eafbdg cgbae cgaefb"},
              {"input": "cbagfed dceba efgcb bcafde gacedb fdca caebf egfabd fa aef", "output": "adegbc cbgfade adcf deabc"},
              {"input": "gcbd bcegad eagdb fedabc acebdgf gcbea gaebdf gacef bc bce", "output": "dbaegc cgfea bcdg ebc"},
              {"input": "cbfdeag agfbce cagef cbdefg gb gefab gcedfa gfb fdeba abcg", "output": "bfg afegb gbf cgab"},
              {"input": "dea fadgbec dcabe abcdeg cfbad gdec agecb gdefab fbgaec de", "output": "dbgfae cdfegab dbgcae beadcg"},
              {"input": "gabcd aebdgc gcaefbd edac gbfad cebag efcbga dc dcegbf cdb", "output": "cbdag agebc afcebg faegcb"},
              {"input": "gacdbe cdabefg fecgab fe gef cbdgef dcfe gdfeb cbegd dagfb", "output": "egf fe efg decgb"},
              {"input": "cbfea bcgf adcfe ecbgad bf gfebad feb bfagce afdcgbe abgce", "output": "cadef bcfg bf dbfcage"},
              {"input": "fabeg cfeab ebgfcad ebfgad eg edag dfbag feg defcbg fbdcga", "output": "efbga fdcegb gbafd gdbecf"},
              {"input": "cdgfba bga geabdc dacge beadf ebgc agcfde bg gbacdef bgead", "output": "cebg fbdae gbec dagfce"},
              {"input": "fbgdace deafcb ead caedg da decgba aefcg bedcg gdbecf badg", "output": "ebfdcg gbad ecagbd egdcb"},
              {"input": "faebg fg gfca eafbd cgbaef baecdfg cedbgf eabcg efg dgceba", "output": "edcgfab feg gf efg"},
              {"input": "adbec dbcaf ecga dea eabfdg cdbge bafdcge bgdcae ae fedcgb", "output": "ead cabdgfe agce egcfbd"},
              {"input": "gdcef agfb bfgade cebdaf debcagf dbafe egbfd cdageb geb bg", "output": "egadbc gcdfe afgb egb"},
              {"input": "gfcbe cgfabe cdagb debgcf de bdef gde dbgcefa dfecag edcgb", "output": "fcegb fdcagbe fcbge edgcbf"},
              {"input": "gaedcf cfedba dgacb cgbeaf fbge ecafg bfdgace gfacb bfa bf", "output": "gcadb decafg adgfec baf"},
              {"input": "eadg gfadbc eagbcd agbcd cea bdafgce cdfaeb ae gcfbe geacb", "output": "ea cdeagb debgacf egad"},
              {"input": "afecgbd eafd adbgf egfdbc cbeag bgfead egafb fe gdacbf efg", "output": "egcab gef dbagfe abgecdf"},
              {"input": "gafbde geab efdcab badef cfdeg gfa egcdafb fdeag ag abfcdg", "output": "fcgde ebfad bgae ebdfa"},
              {"input": "adbef adbcfg fbgace eac ec egcb afcgb cfeab faedgc dgfebca", "output": "gbadfc eca ecgb cgbe"},
              {"input": "fb efadcb fab gbfeca gfcab baecgd fadgc gfedabc gbef cgaeb", "output": "beagdc cabfg bacge gbfe"},
              {"input": "dfabcg bcdg dagbf aegcbfd db fbd gcbaf gefad feabdc gcbeaf", "output": "fagdb bacfdg gabdfc dcgb"},
              {"input": "ecagbdf dgfac cefag geacdb dcefgb df bdcgfa afbd abdcg fcd", "output": "dfc defbcg df afbd"},
              {"input": "bfadc bcgad acegd bg ceagdfb bag cdaefb fcgb cgadfb gdebfa", "output": "cfbadge efbdcag fcdab dcbaf"},
              {"input": "bdcefa gc cgb egdc ecdbf cfdgba agfbe dfgebc cdgaefb gbfce", "output": "cbegf begfc ebcdgf fabge"},
              {"input": "caedgf egf dcebg cfbeg edgafbc bgdf ebdfcg eacdgb gf eafbc", "output": "bgfd efgcb fg afbcegd"},
              {"input": "gbfae cdabfe degc edb cbdfg ed ebdgf dbfgce baecgdf agdfcb", "output": "adcefb ed de cfbgde"},
              {"input": "fdbcge defabcg fgead befda gacedf ag gdca gea cgeafb fdegc", "output": "ga fecgd ga dfegc"},
              {"input": "ed efcgab edacg adcgbe acgefdb deba fcbedg agfdc bgace ecd", "output": "afdcg bceag de gcdeab"},
              {"input": "facdbe dagec bfcea bcd dfcgbe cbdae bd abdf bgcefda cbegaf", "output": "dcb aecbd befac ecfdab"},
              {"input": "fa fea gafc gfebd dcabge dfbaegc gacfeb abgfe baefcd bcgea", "output": "befdg gecfab cafebg agceb"},
              {"input": "cebad ebdgca bd fbedacg gaefdc gadce becaf gebd cfbagd cbd", "output": "dcgfea abcgdf cdb bd"},
              {"input": "cfbgdae cgfdb cabgef df bdfa bgfac gcadef dfc fcgadb egbdc", "output": "df faedgc dcegb dcgbf"},
              {"input": "cbfg gecfa adfbge gfbcdea eabfcd fg bgfeca acedg fga bafce", "output": "efbgac dcfabe cebafd decag"},
              {"input": "gdcbef dcfage acgde fgbea gedbac bc bgace gdaefbc ecb dacb", "output": "abdc bfgea ebfgcd adcbge"},
              {"input": "gafe cfbad aedcfbg adbgce cebgfa agcbe gf gbedcf gcabf gcf", "output": "bcega begcfa gafbc feagbcd"},
              {"input": "cabefg ce ecfb dcebagf gface afged fbcga afcdbg eca cegdab", "output": "aec ec gafecdb bdgcaf"},
              {"input": "bgdcae cedga bdgaecf cd afegd dbac dgc efagcb gefdcb cegba", "output": "efbgca bdecgaf caegbd dgc"},
              {"input": "aebgd cfageb ecdagb beagc bcfdeag dfgab de ebfdcg dge adec", "output": "ed gfebca de fdcegab"},
              {"input": "ebcdagf fcga gfbaed gf dgfaec ecfad adcbef gdcef gbdce feg", "output": "dfcae fge feg fbegcda"},
              {"input": "fba cegadbf fa deaf deabg fedbag dgcbf agebdc gafbd bgfeac", "output": "bfa bfa fgcbead fbedgca"},
              {"input": "cdgef dgbcaf gadcb edacgb agfdc adbfce gaebcfd fa abgf dfa", "output": "gbfdac acfgd gfcda fegdc"},
              {"input": "dcagbf cfda fcdbge cf bafcg bdgace adbcg agebf bcgedaf gcf", "output": "dcbegf bgdac gafcbd cgbda"},
              {"input": "degfac eafcb dfacg gbcaedf gb dfbg afbgc bag bcgeda gfbdac", "output": "dgcefa dgbf bga fcgad"},
              {"input": "deg fgdb feabd dg gefac fedbca eacgfbd ebacgd abedgf dfaeg", "output": "egfda gadfe edg dfbae"},
              {"input": "degf fcagde cgdebaf cgf cafgd gf fadce cgfeba gcbda fcaebd", "output": "cdbag bdcag egdf dacgb"},
              {"input": "fdgb bagfdc dbcaf fb abdceg fba fbeacgd geafcb afdce bgadc", "output": "bf fba dbafc gadcb"},
              {"input": "aegdb fdagceb bafce fad dgabfe df cagbed fdeg aefdb gfacdb", "output": "becgad adfbe afd badfe"},
              {"input": "fdbg gfabc fcabd fd abcegf gadbcfe ebcad dcf dcfbga fagdec", "output": "bagcfe gfacbe fd cagebf"},
              {"input": "cgfd egdca fdaceb abegd egabcf eacfg ecbfgda dca fdcage dc", "output": "egcaf ecbdgfa abcfed dcgf"},
              {"input": "efdgba cgfeda ac gabecdf efagd adcef fac cefbd gcea dagbfc", "output": "afebcdg ca bcfed ca"},
              {"input": "acbfeg bg fecbgd fgdeac acebgfd gbe bagc afecg fbead begfa", "output": "agcbdfe bg fegba badegfc"},
              {"input": "eadbgc edfba bfecdg acfb egfad ba bea dfceb dcaebf beagdcf", "output": "ab eafbd abe adcfgbe"},
              {"input": "fbega afdce gd agcebf becgad bgdeaf fbgd gde ebgfdca efgad", "output": "cegdab cefbga fbgd geadf"},
              {"input": "cag agfce gfacde gbcdaf ag gead fbgec cdefa bdafcge bdefac", "output": "cfead gca adge bdagcf"},
              {"input": "dc cebfa egacfdb dcf edbfc cbdgfa fdebg gefdba cged fdecbg", "output": "dcf eafbc bgacdf dc"},
              {"input": "edbfg fdacge dcgae baegcd bacfgd ecaf geabdfc ecdfg fgc cf", "output": "defcag dbfgca ebfdcga cebdga"},
              {"input": "fdgec gd gfd efcbd fdagbc bedg fabedgc gaefc becadf fdbecg", "output": "gacfbd fbdcag dgbe edcbf"},
              {"input": "fec dgebf fbdc efbdcga afegcd befagd fdcgeb fc egcfb cgeab", "output": "bdefgc dfegba degabfc fc"},
              {"input": "cdb gdfc dc cbdega eadbf egfacb gfcebad cgbfda acbdf bagfc", "output": "dgaecb cd bafed dcb"},
              {"input": "dcbga ag cgdaef fgbdeac daebc fbag cag fgcdb ebfgcd fbcgad", "output": "ag faegcdb acgdfe dfgcba"},
              {"input": "dabef fa ebacfd dfa bdfec fbgdca cbfegd dbcegaf bgaed efca", "output": "gdaeb afd eadbf fa"},
              {"input": "bed dgab gfced afgbedc dfbge geafb efadbc febdga cafgeb db", "output": "fgeba gdba aegfcb gfecd"},
              {"input": "da gbacf becdaf ebcfgad ecad cgfbde fedgab dbfca fecbd abd", "output": "ad egbfdc bad fcbag"},
              {"input": "efc bgfceda dfbcag ecbg efagd acbgf fbagec aecfg ce bfeacd", "output": "egfac ec afecgb fbeacgd"},
              {"input": "aedfbc gaced fabg ab bdgfc gefbcd adb gdbac acdegbf gcfbad", "output": "ba bcgdf ebfcda bafegcd"},
              {"input": "cdgfb abegdc fgeacbd feba ecafgd gebfda ef efd dbfeg bdeag", "output": "dfe egfdb agefdb bedga"},
              {"input": "cagfb ef fcdgae cfe cgafdb bcedg fbdgcae bcegf feba acgfeb", "output": "gefdac egfacd cgebd feadbgc"},
              {"input": "bfgedca cabfgd gbac ebdfa ag abgfd dga egfdac bdcgf gbcefd", "output": "cafged bgadf ceafgd ag"},
              {"input": "gebda bc eagdbfc ebdcg cdbgfa cgb ecdgfa cefb gfdec fbgecd", "output": "dfgbac cebf dgbecf fcbgade"},
              {"input": "dfbcag dafgc bfd fdgcae gebda ecafbd gfadb gfcb fb dacgbef", "output": "gbdfa dagcf dagfc fbaced"},
              {"input": "cd dfebg fcdgb cadb gdeacf eafcbgd gfceab cdg abgcf dgbfca", "output": "dc fbadcg cd adbc"},
              {"input": "becafd dbfa feb fb abgcef adgefc cefda bgced edcfb bedgfac", "output": "fcdabe bf feb dfab"},
              {"input": "gbadfe fdcage acgef fed ed decg abgfce adcef gebfadc fabcd", "output": "ecdg afbcd afdgce fde"},
              {"input": "fcaedb dgbca fdcg efgbdca fbgca befag caf bagfdc dbaegc fc", "output": "fca gfacb bgceda fc"},
              {"input": "cabed fbed fd cfd fagecd bfdca bfcdaeg acfgb bedcaf dcgbea", "output": "aebfdc ebfd bdcaf fcdgea"},
              {"input": "agdbfc fagbc fgdc dgacebf bcgaef fda ceabd bdfca fbgead fd", "output": "fda fdcegab bgafc edbafg"},
              {"input": "cbgfa bfdgea bfdgc ga fga aecbdf gcae egbcaf bcfgdea cefab", "output": "ga fcabe fgbdc gfbac"},
              {"input": "cgafe cbagdfe afbce afegdb efgda gebcda gc gdcf cag eagdcf", "output": "befca gafed eadbcg gca"},
              {"input": "agfce edgcba egbac gcbf fagbde gdacebf agf cdaef gbeacf gf", "output": "fecag bgace gdfbaec bgcfdea"},
              {"input": "be gaeb gdeaf fcdab cbegfd fgeacd efdab fbe cgebfda dagebf", "output": "feb dfgacbe faedcg egfbad"},
              {"input": "dfcba cgfdbae gda afedcb bgca bagcfd ga gbdef eadcfg bgafd", "output": "bgfad gfebd ag efabdc"},
              {"input": "edgafb dgef agbedc gf abfgec fcdgeba adfbg abdeg fga cfbda", "output": "dafecbg badfg bcagdef fag"},
              {"input": "fgc cgfbe ebgaf cbfa cgedbfa cf bgced gecfab defbag fgdcae", "output": "gfc cgf gbdfea fcg"},
              {"input": "cga bcadfge aefdgc edgca dafc gdafbe aefcbg agefd ca cdegb", "output": "debcg faecgb cga gac"},
              {"input": "dbcaf gcadebf eafcgb dbcefa gbdf cbfdga bcg adbcg gb edacg", "output": "afecbg cbg bfcad cabfdg"},
              {"input": "fd dgaeb def fgecb fdebac feadbg eabdgc dfgeb becfdga gafd", "output": "fbgce egadb bdgea fagd"},
              {"input": "cedbgf dbcgf febcad dgeafcb efcagd bfge cfg bdcga dbcfe fg", "output": "gcf cbgda gcf cadfegb"},
              {"input": "gfabc agc degbaf fgaecb gaefb ca cefa bedgac fedgbca gcfbd", "output": "begdca gbdcf cag eacf"},
              {"input": "ebfa be fgbcd afcegd cbe febcd faced egfdcba dbface aecbgd", "output": "ceb ceb cbfadeg feab"},
              {"input": "gbfad cdeabgf bdeag de afcdge ade cdbe ebacg geafbc adcbeg", "output": "cbdefga gaceb ed bdce"},
              {"input": "fcedbag adfeg fadebg cbgda fdeb fba bf egdcfa gfadb cfbgae", "output": "bf fegad gabdf dgcba"},
              {"input": "abde debfgca acfegd ae fgcbe dabgc gbadfc cgeba cgeabd aeg", "output": "eag bcfgdae gfebc aegbc"},
              {"input": "afdeb caegfd dcgb bcafge egabfcd fgd cgfbad dgbaf fcgab gd", "output": "aebdfgc bcdg agfebcd fdabg"},
              {"input": "ecbafg acdbfe bfge cfaeb cedga cfega dafgbc afg gf bcfgaed", "output": "cbdfga fg efagc geacf"},
              {"input": "ecafbg adgfecb fdeac agbd cbgdf cfgbda agf ag bedcgf agcdf", "output": "ga ga fag cfdbg"},
              {"input": "gcdbe cbadefg cdf dfea df gfaebc facbed cfbae bagcdf ebfdc", "output": "afde aecfb cbfdea caedfgb"},
              {"input": "gcfb beafgd fdg deagc cfbed fg gacdfeb gdcbef fcebad gedfc", "output": "cdbef dgf dfg bcfdgea"},
              {"input": "dgebfac eacdbf bdc abgdc adbeg cadgf cbfg cegfad gcbfda cb", "output": "cafdeg fdacge facgd bcd"},
              {"input": "cdeag becf fgdbac fc gbfaced edgfc dgebaf gbfdec edgfb cgf", "output": "gafdeb daegc bcdfge egdfab"},
              {"input": "aegd cgd abfcd cabgde fdegbc dg ecagb dagfbec cbegfa badcg", "output": "ecagbfd debcgf agde bacfd"},
              {"input": "cfdge gb abfed bdg cbge gfedb bgfcdae cbdagf begcdf fcdega", "output": "cgbe bgd cfbgda fcedg"},
              {"input": "egdfca eafdcb ecdag dbgfac gefa ag bcfadge agc gcbed dacfe", "output": "ebafcdg acefd fdcae agc"},
              {"input": "afbgec edgb dafeg fegab agfdc de eda fbdgcea dfaecb fdegab", "output": "ead aed cfebad bceafg"},
              {"input": "dbgc gbeaf acfebd agd afecbgd fabdc ceagfd gbfda cbfagd dg", "output": "gcdb efdacb gfdbca gbdc"},
              {"input": "afcedg gbad dgecb gcefb acdbeg dg abedc dcg dabcef gbdcfea", "output": "cgdeaf beacfd cbade cgdbe"},
              {"input": "ea egfdba dgceaf daec cfgbe eag befgdac fegca cadfg fabgdc", "output": "fgceb adfgc abcfgde gaefcd"},
              {"input": "agdebfc dbgca egb egfd abfde agdfbe fcbade fgeabc dgbea ge", "output": "bdgca debaf aedgb fegacb"},
              {"input": "efcbd ecgd fbecgd adgbf egacbf bfcgdae ebg fdebg ge dcebfa", "output": "gfceba cbdfeg eg fgceadb"},
              {"input": "dc befgac cdb aced gcbfead dcgefb adfbg acgbd cabeg eacdbg", "output": "edcabg bdc dgcaeb acbgefd"},
              {"input": "afgbc dbaf ebcfg ba ecfgdab adcfg bca fcaegd cgabdf gcabed", "output": "bfgce egadbc cbgaf acdbefg"},
              {"input": "cagbd adg cegafd acfgebd bdaec gbfd gd gbafdc bgacf faegcb", "output": "gebacf dg gda agdbc"},
              {"input": "bc cdgba adfcg ebadg cfbdae ebfgad dgbfcea cba bgec gbdace", "output": "bc cb dafgeb cab"},
              {"input": "gae bfegc edfac gdca ga begdaf cgeaf edafcg bafedc cfbedga", "output": "adfcge ecdfag fabcde aecfdb"},
              {"input": "cdfge db eabcf fdb bade cbfed cbfdaeg gfbdca dcbefa cgfabe", "output": "dbf cbagdef db abed"},
              {"input": "efa facg beadcg gacfde cbfed dcefbag adceg fa gedbfa cfdea", "output": "agecd gcbaed afcde eacdg"},
              {"input": "dbgca dfbeg fcg adbcgf bafgce fdca cgbdf gabdcfe dbecga cf", "output": "gacefb cabdg dfca fcg"},
              {"input": "dbfcae gc decg ebadc cga abegf cbfaegd cbage gabfcd agdebc", "output": "edbcga gebca cebda baegdc"},
              {"input": "becagd gefcdba bgaef gfadcb fgd fadc bdacg dfagb fd ecdbgf", "output": "dgf fgaeb cdaf fd"},
              {"input": "egfcab dcfgea caebg ag cbeafd edfabgc gfba bcdeg acg ecafb", "output": "cfbaeg gac acgfed eabcg"},
              {"input": "gbc gfbad fgbac beadgf cg fbeac gdfbce dbgcaf bgcfead cgda", "output": "gacd edfgbc cbg gafbed"},
              {"input": "fgdba begcad fg gfd fdacb debfag egdba adfcbge fgbedc afeg", "output": "afdbg bdaeg badfg eagcdb"},
              {"input": "cefgdb fdecga beafg agd acbd badge cgfdeba cebdg ad dacbeg", "output": "cabd cedafg cfedag fgaeb"},
              {"input": "fgc cdefb beafcg dcfbg adbgfe cgad acefbgd adbfg cg afdgcb", "output": "fegcdab bagfecd gfdcb gcad"},
              {"input": "cbagfe cbedgaf bfgde cfdeab gfeba df fgda dcbeg afebgd bfd", "output": "fd adfg ebgcd fcabge"},
              {"input": "ebgaf ad ebacgd adfgb cadf abfdcg badgecf cdgfb bad ebcgfd", "output": "bdegcfa cfda fbaeg gbcfad"},
              {"input": "adfcg dabecg gaebfcd ecfbag bgacf gdc bgdf cbfagd eadcf gd", "output": "dg cfgab fcgab agbfce"},
              {"input": "ecfgdb dcgbfa fdage ecda ad ebfag dfa bfadecg fadecg cegfd", "output": "ad dgefc cdae bgdecf"},
              {"input": "agcfed eabdfcg aec ce gacbd gadec geafd cefd bagdef cgafbe", "output": "ce aefbdgc egcbfa gaecfd"},
              {"input": "gdace fe bdgafc efa dbafecg fgeb bdafce beadfg egdfa dgfab", "output": "ecgda fe fbgad fedabg"},
              {"input": "fg bdgcefa gabed defga fbeacd bdcafg cfeg gfd edcfga fdeac", "output": "agfde fg fcbade dfgea"},
              {"input": "dcgfbe egdfc gcbd dc geafd becdaf gcabfe cde efbcg gedbfca", "output": "dc fgead dgcef gdcb"},
              {"input": "gdefa efadbc cfdebga adfebg eaf ebag ea adfbg cfdeg acgfdb", "output": "fgdbaec cabgfed dgafe efa"},
              {"input": "fecb fcegbda dgeaf eagdbc eb dbegfc cfgbad beg gbedf fbgdc", "output": "bcef dfegb gbdfca dgcbafe"},
              {"input": "befg bafde afgdc degfa cdeafbg edafbc dge eagcdb gdbafe eg", "output": "dge efbad becgda aegdbf"},
              {"input": "ac adfgc cedfg bedgac cda ecfagd degbcf fecabdg afec badfg", "output": "gdfab dcgaf fgced cegafdb"},
              {"input": "cda badcg edcgb geca ca bdaegc dbfaec decgbf agfbd ecdgfab", "output": "ac bdfag ca edgbfc"},
              {"input": "fgac febgca fg ebacf bgfecd gfb gbcfdea badeg bfage bedfca", "output": "gbefcda fg bdfceg gcfa"},
              {"input": "bcgfade ce fcge dbgcfa cdafe badgec acgfd gceadf befad edc", "output": "bagcfed ecfda fcgad dce"},
              {"input": "ebacfg efbad fcbaedg age dfagc adefg cdge eacgfd ge dgfabc", "output": "geabfc cdfagb eafdgc gae"},
              {"input": "abd cgbde da gdcaeb cagd baecd faceb afdebg ceagbdf egfdbc", "output": "agdc gadc gedbcaf bcafe"},
              {"input": "eg bdfgec dcfbe facebg efg gabcedf dcgfe cedfab afgcd debg", "output": "ecgdf cgefbd cdgef feg"},
              {"input": "eagf efbdgc dga dcefg cdgfea bcdea cdgfab ga gdeafbc ecdga", "output": "gcdae aedgc ga ecdab"},
              {"input": "ga cbedg eacfdg acg eabdcf ebafgc adgf cfeda egadc dacefbg", "output": "dfag fbcage bafgce acgde"},
              {"input": "gfea cgdfeb efabc agfedcb gfc afegbc gf cdfbae abgfc dcbag", "output": "caebdf beafcd caebgf baecf"},
              {"input": "efd gefa gedcab dcfab cfdea ecdgafb fbdceg egdfac ef agcde", "output": "gafcde ef aefg cadfb"},
              {"input": "bafecdg deafbg fadeg bga deagbc gebfc bafd efbag ba dcgeaf", "output": "gedaf ba dgbaecf ba"},
              {"input": "ag dga geabfd becadf gbaecd abecd aceg bagcd cfgdb cebdgaf", "output": "egfbad aegbcfd cgae dacbe"},
              {"input": "bcdgeaf gbfda afcged gfebd fa dgfcbe efab agf bdcga dafgbe", "output": "gafedb efbgda ecagfd fgdbe"},
              {"input": "degafc feba fgbcde bafegcd bge adegb be dfega efadgb cgbda", "output": "dbegcfa acbgd faeb acefdg"},
              {"input": "gdcfeb ea fceab fgbca adfbeg eadc cdebafg cebdf aef fecabd", "output": "cefba fae dcea efa"},
              {"input": "agfde dbega fg dcfg ecadfb cegbaf adfec adecgf adebgcf agf", "output": "dgfc gcfade afbecg dcfage"},
              {"input": "fbade caebg becadf fgdb gfa dafgbec fg afgeb fbeagd gaedfc", "output": "eacfbd bgeafcd fg efbad"},
              {"input": "gbdacf aefd ed geadcf cegfd fcgeadb dbeacg cadgf ecgfb dge", "output": "gbacfd beacgd ecgadf cgfbda"},
              {"input": "adebgf gdf cefgdba fd gcfba efad dbgeca agebd afgbd fdegbc", "output": "deaf gfbdea df dbaeg"},
              {"input": "adgbf cbfg fagde facebgd gbd acdbf badegc baecdf gbfdac gb", "output": "bdagfc gcfabed fdcab cdfab"},
              {"input": "dbgace cbdfg ab dfagb abef abgfde gaedf bad ecdafg gcdbeaf", "output": "ba cbaedg ba dfbga"},
              {"input": "bgcade acbedgf gbef cef cdbfa ef cbefd afgecd bgdce fbcgde", "output": "ef ef fce dgecfba"},
              {"input": "gbfced abegc cde acbde fcgaeb cd gebacd agcd gfabdec abdef", "output": "gdca gacd dcbae bdegafc"},
              {"input": "gb facdb fedcab fgb gadebf aegfc dgcb cabdgf gbcfa eafcgdb", "output": "fegbad adfcb dafgbe fdcba"},
              {"input": "gfbaed fcabde gdbfc bdeafgc dgb agfcdb cgda fcdab gfbec gd", "output": "becadf facdeb dg agbdcf"}]

# Task 1
def find_unique_output(data):
    nbr_of_unique = 0
    for d in data:
        word_list = d["output"].split()
        #print(f"word_list: {word_list}")
        for word in word_list:
            if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
                nbr_of_unique += 1
    return nbr_of_unique

def get_value_of(word):
    if sorted(word) == sorted("acedgfb"):
        return 8
    elif sorted(word) == sorted("cdfbe"):
        return 5
    elif sorted(word) == sorted("gcdfa"):
        return 2
    elif sorted(word) == sorted("fbcad"):
        return 3
    elif sorted(word) == sorted("cefabd"):
        return 9
    elif sorted(word) == sorted("cdfgeb"):
        return 6
    elif sorted(word) == sorted("eafb"):
        return 4
    elif sorted(word) == sorted("cagedb"):
        return 0
    elif sorted(word) == sorted("ab"):
        return 1
    else:
        print(f"word: {word} is not supported!")
        return 0

def decode_string(data):
    word_list = data.split()
    total_val = 0
    for i, word in enumerate(word_list):
        word_val = get_value_of(word)

        total_val += (10**(3-i))*word_val

    return val


#result = find_unique_output(input_data)
#print(f"result: {result}")
#
#val = decode_string("fdgacbe cefdb cefbgd gcbe")
#
#print(f"val: {val}")


# Task 2:

# test_data = [{"input": "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb", "output": "fdgacbe cefdb cefbgd gcbe"},

def sort_word_letters(list_of_strings):
    #print(f"B list_of_strings: {list_of_strings}")
    sorted_strings = []
    for string in list_of_strings:
        sorted_strings.append(sorted(string))
    #print(f"A list_of_strings: {sorted_strings}")
    return sorted_strings


def word_containing_letters(word, letter_list):
    if(all(x in word for x in letter_list)):
        return True
    return False


def get_lower_left(word_list):
    # four occurences in 10 numbers
    number_of_letters = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
    for number in word_list:
        if 'a' in number:
            number_of_letters['a'] += 1
        if 'b' in number:
            number_of_letters['b'] += 1
        if 'c' in number:
            number_of_letters['c'] += 1
        if 'd' in number:
            number_of_letters['d'] += 1
        if 'e' in number:
            number_of_letters['e'] += 1
        if 'f' in number:
            number_of_letters['f'] += 1
        if 'g' in number:
            number_of_letters['g'] += 1

    for key in number_of_letters:
        if number_of_letters[key] == 4:
            return key
    # for loop should always return!
    print("!!!!ERROR!!!!!")


def get_decoder(input_string):
    result = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "0": ""}
    word_list = sort_word_letters(input_string.split())
    nbr_of_six_letter_words = 0
    nbr_of_five_letter_words = 0
    lower_left = get_lower_left(word_list)

    # Get known first
    while len(word_list) > 6:
        for i, word in enumerate(word_list):
            if len(word) == 2:
                result["1"] = word
                print("1 found")
            elif len(word) == 3:
                result["7"] = word
                print("7 found")
            elif len(word) == 4:
                result["4"] = word
                print("4 found")
            elif len(word) == 7:
                result["8"] = word
                print("8 found")
            else:
                continue
            word_list.pop(i)

    while len(word_list):
        for i, word in enumerate(word_list):
            if len(word) == 6 and nbr_of_six_letter_words == 0 and not word_containing_letters(word, result["1"]):
                nbr_of_six_letter_words += 1
                result["6"] = word
                print("6 found")
            elif len(word) == 5 and nbr_of_five_letter_words == 0 and word_containing_letters(word, result["1"]):
                nbr_of_five_letter_words += 1
                result["3"] = word
                print("3 found")
            elif len(word) == 6 and nbr_of_six_letter_words == 1 and word_containing_letters(word, [lower_left]):
                nbr_of_six_letter_words += 1
                result["0"] = word
                print("0 found")
            elif len(word) == 6 and nbr_of_six_letter_words == 2:
                result["9"] = word
                print("9 found")
            elif len(word) == 5 and nbr_of_five_letter_words == 1 and word_containing_letters(word, [lower_left]):
                result["2"] = word
                print("2 found")
            elif len(word_list) == 1:
                result["5"] = word
                print("5 found")
            else:
                continue

            word_list.pop(i)
            #print(f"A result: {result}")
            #print(f"A word_list: {word_list}")

    return result


def decode_output(decoder, data):
    result = 0
    word_list = sort_word_letters(data.split())
    for key in decoder:
        for i, word in enumerate(word_list):
            if decoder[key] == word:
                result += (10**(3-i))*int(key)
                #print(f"result: {result}")
    return result

total = 0
for data in input_data:
#for i in range (0,1):
    print(f"input: {'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd'}")

    decoder = get_decoder(data["input"])
    total += decode_output(decoder, data["output"])

print(f"result: {total}")


## Unique number of letters
#ab: 1 --> a and b in right
#abd: 7 --> d is top
#abef: 4 -->  ef is upper left and middle horiz
#abcdefg: 8 --> cg bottom left and bottom
#
#Known:
#if 2 letters: 1
#if 3 letters: 7
#if 4 letters: 4
#if 7 letters: 8
#if 6 letters but not containing 1: 6
#if 5 letters and containing 1: 3
#get_lower_left() # four occurences in 10 numbers
#if 6 letters and lower_left: 0
#if 6 letters: 9 (only one left)
#if 5 letters and lower_left: 2
#only one left: 5


##unique only
#abcdf: 3 (right top, right bottom, top)
#acdfg: 2 (top)
#bcdef: 5 (top, upper left, middle)
#
#abcdeg: 0 (right top, right bottom, top) (Could I verify that this only miss one of the letters in 8? and that one of these are ef of ab? then that provides: f --> middle and thus e --> upper left)
#bcdefg: 6 (top, upper left, middle) + (bottom left and bottom).  (missing: bottom right) only a missing then a --> upper right and b --> lower right
#abcdef: 9 (right top, right bottom, top, upper left, middle) g missing: (bottom left of bottom)
#
#a or c: 8
#b: 6 (upper_left)
#d or g: 7
#e: 4 (lower_left)
#f: 9 (lower_right)
#
#
#  0:6    1:2     2:5      3:5    4:4.     5:5    6:6     7:3     8:7      9:6.
# aaaa    ....    aaaa    aaaa    ....    aaaa    aaaa    aaaa    aaaa    aaaa
#b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
#b    c  .    c  .    c  .    c  b    c  b    .  b    .  .    c  b    c  b    c
# ....    ....    dddd    dddd    dddd    dddd    dddd    ....    dddd    dddd
#e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
#e    f  .    f  e    .  .    f  .    f  .    f  e    f  .    f  e    f  .    f
# gggg    ....    gggg    gggg    ....    gggg    gggg    ....    gggg    gggg.
#
#  5:5    6:6     7:3     8:7      9:6.
# aaaa    aaaa    aaaa    aaaa    aaaa
#b    .  b    .  .    c  b    c  b    c
#b    .  b    .  .    c  b    c  b    c
# dddd    dddd    ....    dddd    dddd
#.    f  e    f  .    f  e    f  .    f
#.    f  e    f  .    f  e    f  .    f
# gggg    gggg    ....    gggg    gggg.
#
# occation of:
# a position exist in : 8  numbers ( this only happens for 2 positions: upper or lower left)
# b position exist in : 6  numbers ( this only happens for 1 positions: MUST BE upper left )
# c position exist in : 9  numbers ( this only happens for 1 positions: )
# d position exist in : 7  numbers ( this only happens for 2 positions: )
# e position exist in : 4  numbers ( this only happens for 1 positions: )
# f position exist in : 8  numbers ( this only happens for 2 positions: )
# g position exist in : 7  numbers ( this only happens for 2 positions: )
