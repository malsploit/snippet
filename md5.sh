for i in *; do sum=$(echo -n "$i"|md5sum); echo -- "$i" "${sum%% *}.${i##*.}"; done
