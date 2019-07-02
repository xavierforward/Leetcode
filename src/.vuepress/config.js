module.exports = {
  title: 'LeetCode题解',
  description: '个人LeetCode题解',
  post: 8081,
  base: '/Leetcode/',
  markdown: {
    lineNumbers: true
  },
  themeConfig: {
    nav: [
      { text: 'Home', link: '/'},
      { text: 'Github', link: 'https://github.com/zhaozecheng'}
    ],
    sidebar: {
      // fallback
      '/': [
        '',
	'/1_two_sum',
	'/2_add_two_numbers',
	'/3_longest_substring_without_repeating_characters',
	'/4_median_of_two_sorted_arrays',
	'/5_longest_palindromic_substring',
	'/6_zigzag_conversion',
	'/7_reverse_integer',
	'/8_string_to_integer',
	'/9_palindrome_number',
	'/10_regular_expression_matching'
      ]
    }
  }
}
