for i in *; do sum=$(echo -n "$i"|md5sum); echo -- "$i" "${sum%% *}.${i##*.}"; done
cut -d @ -f 2 yourlist | sort | uniq -c | sort -rn
cat domenii | xargs -n1 -I {} -P8 sh -c   'curl {} -LI -s -o /dev/null -w "{},%{http_code}\n" -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" --max-time 60 "$@" '
