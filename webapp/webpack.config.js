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

    new webpack.DefinePlugin({
      // global app config object
      config: JSON.stringify({
        apiUrl: 'http://localhost.charlesproxy.com:8000'
      })
    }),
    new BundleTracker({filename: '../webpack-stats.json'}),
  ],
  // optimization: {
  //   splitChunks: {
  //     chunks: 'all',
  //   },
  //   runtimeChunk: true
  // },
  output: {
    path:  path.resolve('../web/static/bundles/'),
    filename:  "[name].[hash].js",
    chunkFilename:  "[id].[hash].js",
    crossOriginLoading:  false,
    publicPath:"/static/bundles/"//1
},
  devServer: {
    historyApiFallback: true,
    publicPath: "http://127.0.0.1:4200/",//2,
    headers: {
      'Access-Control-Allow-Origin': '\\*'//3
    }
  }
};
