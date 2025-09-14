read -p "Enter Base64 string to decode: " input_string
echo "Decoded Output:"
echo "$input_string" | base64 --decode
