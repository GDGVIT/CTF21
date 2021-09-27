base64 -d dist/flag > flag_bin
chmod +x flag_bin
echo "goodbye" | ./flag_bin
rm flag_bin
