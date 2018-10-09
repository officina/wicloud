const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');
var path = require('path');

module.exports = {
  context: __dirname,
  entry: './src/main.ts',
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: ['ts-loader', 'angular2-template-loader'],
        exclude: /node_modules/
      },
      {
        test: /\.(html|css)$/,
        loader: 'raw-loader'
      },
    ]
  },
  resolve: {
    extensions: ['.ts', '.js']
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: 'index.html',
      inject: 'body'
    }),
    new webpack.DefinePlugin({
      // global app config object
      config: JSON.stringify({
        apiUrl: 'http://localhost.charlesproxy.com:8000'
      })
    }),
    new BundleTracker({filename: '../webpack-stats.json'})
  ],
  // optimization: {
  //   splitChunks: {
  //     chunks: 'all',
  //   },
  //   runtimeChunk: true
  // },
  output: {
    path:  path.resolve('../web/static/webpack_bundles/'),
    filename:  "[name].bundle.js",
    chunkFilename:  "[id].chunk.js",
    crossOriginLoading:  false,
    publicPath:"/static/webpack_bundles/"//1
},
  devServer: {
    historyApiFallback: true
  }
};
