const webpack = require("webpack");

const plugins = [
      new webpack.ProvidePlugin({
        'window.jQuery': 'jquery',
        'window.$': 'jquery',
        $: "jquery",
        jQuery: "jquery"
    })
];


module.exports = {
  plugins: plugins

};
