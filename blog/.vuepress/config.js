module.exports = {
    title: 'Leetcode题解',
    theme: "@vuepress/theme-blog",
    base: "/leetcode/",
    plugins: [
    ],
    themeConfig: {

        dateFormat: 'YYYY-MM-DD',
 
        /**
         * Ref: https://vuepress-theme-blog.ulivz.com/#footer
         */
        footer: {
            contact: [
                {
                    type: 'github',
                    link: 'https://github.com/xize1993',
                }
            ],
            // copyright: [{
            //         text: 'Privacy Policy',
            //         link: 'https://policies.google.com/privacy?hl=en-US',
            //     },
            //     {
            //         text: 'MIT Licensed | Copyright © 2018-present Vue.js',
            //         link: '',
            //     },
            // ],
        },
        directories:[
          {
            id: 'post',
            dirname: '_posts',
            path: '/',
            itemPermalink: '/:year/:month/:day/:slug',
          },
          {
            id: 'writing',
            dirname: '_writings',
            path: '/',
            itemPermalink: '/:year/:month/:day/:slug',
          },
        ],
        /**
         * Ref: https://vuepress-theme-blog.ulivz.com/#sitemap
         */
        sitemap: {
            hostname: 'http://xize.space/'
        },
        smoothScroll: true
    }
}