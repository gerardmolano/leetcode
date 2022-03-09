var lengthOfLongestSubstring = function(s) {
    let chars = {}
    let j = 0; // start of substr
    let len = 0;

    for (i = 0; i < s.length; i++) {
        let char = chars?.[s[i]];

        if (char === undefined) {
            chars[s[i]] = 0;
        } // if

        j = Math.max(chars[s[i]], j);
        len = Math.max(len, i - j + 1);
        chars[s[i]] = i + 1;
    } // for

    return len;
};

// test here
console.log(lengthOfLongestSubstring('pwwkew'));
