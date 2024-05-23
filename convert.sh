for f in ./r9k/*
do
	v=`file "$f"`;
	n=`basename "$f"`
	echo "$n"
	if [[ "$v" == *"ASCII"* ]]; then
		
		iconv -f "ASCII" -t "utf-8" "$f" -o "./r9k/converted/$n"
	else
		cp "$f" "./r9k/converted/$n"
	fi
	echo $v
done
