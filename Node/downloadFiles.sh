declare -a urls=()

Cmd="curl  -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, sdch, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Referer: https://www.hackerrank.com/challenges/compare-the-triplets/leaderboard' -H 'Cookie: optimizelyEndUserId=oeu1464714544282r0.7679238451873855; hackerrank_mixpanel_token=c57eefae-8e7a-42f6-a9aa-443ca882fbad; enableIntellisenseUserPref=true; blackrock-codesprint_crp=*nil*; _biz_flagsA=%7B%22Version%22%3A1%2C%22Frm%22%3A%221%22%7D; interstate_v2_efa8dff896d3b51999c6e1eae8719e46b2a36441=%7B%22user_identifier%22%3A%2250c7af53-1f210787-b15a58ff-97a48042%22%2C%22last_updated%22%3A1464714544562%2C%22utm_campaign%22%3Anull%2C%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_term%22%3Anull%2C%22utm_content%22%3Anull%2C%22last_visit%22%3A1469174506783%7D; hackerrankx_mixpanel_token=e2513da2-796a-4679-a94a-281684ec92fd; mp_dcd74fdb7c65d92ce5d036daddac0a25_mixpanel=%7B%22distinct_id%22%3A%20%22e2513da2-796a-4679-a94a-281684ec92fd%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _mkto_trk=id:487-WAY-049&token:_mch-hackerrank.com-1474913574438-41852; olfsk=olfsk5045541781871208; hblid=RJMp1dt988rEdicS462116IpDJR30ENG; _hp2_id.547804831=%7B%22userId%22%3A%225542007655523010%22%2C%22pageviewId%22%3A%220965321578641348%22%2C%22sessionId%22%3A%220384269648757137%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; mp_36cfc98842f47eba17d79df294c189f0_mixpanel=%7B%22distinct_id%22%3A%20%22157672e8a8b4c0-062a5029bee074-3d654c0f-130980-157672e8a8c414%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.hackerrank.com%2Fchallenges%2Fcompare-the-triplets%2Fleaderboard%22%2C%22%24initial_referring_domain%22%3A%20%22www.hackerrank.com%22%7D; default_cdn_url=hrcdn.net; optimizelySegments=%7B%221709580323%22%3A%22false%22%2C%221717251348%22%3A%22gc%22%2C%221719390155%22%3A%22search%22%2C%222308790558%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; remember_hacker_token=BAhbB1sGaQPEawlJIgAGOgZFVA%3D%3D--cc0833178e11b41ce3987a1ded340bddfd183455; metrics_user_identifier=96bc4-c85a9248ec5e3b4e3e709222991c0aee2b0979c5; _hrank_session=780f7c52327c4424ed7b406bceabadc34005af14e3bcfd5c433056199dcda1f3b9f3a0c8fb4f5c7a8a0d46182090ea378c9ab0ddb4c5e91dc41a6e3e7d1d8820; __utmt=1; session_id=ivveejd0-1474992590104; cdn_url=hrcdn.net; cdn_set=true; h_r=domains; h_l=_default; h_v=_default; hr_domains-master=algorithms%2Cwarmup; hacker_editor_theme=light; _biz_uid=4ce718296a4444bfdd01f705ca1920a8; _biz_sid=33236d; mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%22c57eefae-8e7a-42f6-a9aa-443ca882fbad%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.hackerrank.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.hackerrank.com%22%2C%22%24search_engine%22%3A%20%22google%22%7D; _bizo_bzid=1814d760-b480-4bee-8ca6-f842294ee98d; _bizo_cksm=B65DA883B23F661D; _bizo_np_stats=14%3D1328%2C; _biz_nA=299; _biz_pendingA=%5B%5D; mp_mixpanel__c=12; __utma=74197771.967646130.1464714557.1474996023.1474999820.34; __utmb=74197771.8.9.1475000275951; __utmc=74197771; __utmz=74197771.1468414457.22.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed"

for i in "${urls[@]}"
do
        curlCmd="${Cmd:0:4} $i ${Cmd:5}"
        response=`eval $curlCmd`
        respStr=$response
        check=${respStr:0:5}
        #echo "$check"
        if [[ "$check" != "<html" ]];
        then
                #tmp=${i/%\/download_solution/.cpp}
                #tmp1=${tmp/%\/download_solution/.cpp}
                if [[ $i =~ ((hackers)).*[^\/download_solution] ]]
                then
                        printf "$respStr" >> "./data/compare-the-triplets/cpp/${BASH_REMATCH:8}.cpp";
                        #echo "$respStr"
                fi
        fi
done