for i in *; do sum=$(echo -n "$i"|md5sum); echo -- "$i" "${sum%% *}.${i##*.}"; done
cut -d @ -f 2 yourlist | sort | uniq -c | sort -rn
