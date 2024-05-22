for f in ./r9k/*
do
	v=`file "$f"`
	if [[ "$v" == *"ASCII"* ]]; then
		echo "basename $f"
		
		iconv -f "ASCII" -t "utf-8" "$f" -o "$f"
		
	fi
	echo $v
done
