const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');

var path = require('path');
var environment = process.env.NODE_ENV === 'production' ? 'production' : 'development';
var API_URL = {
    production: 'http://wicloud-test.wi4b.it/wicloud/api',
    development: 'http://127.0.0.1:8000'
}

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
    new webpack.HotModuleReplacementPlugin(),

    //new CleanWebpackPlugin(path.resolve('../web/static/bundles/')),
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: 'index.html',
      inject: 'body'
    }),
    new webpack.DefinePlugin({
      // global app config object
      config: JSON.stringify({
        apiUrl: API_URL[environment]
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
    filename:  "[name].bundle.js",
    chunkFilename:  "[id].bundle.js",
    crossOriginLoading:  false,
    publicPath:"/static/bundles/"//1
},
  devServer: {
    contentBase:  path.resolve('../web/static/bundles/'),
    historyApiFallback: true,

    hot: true,
    //publicPath: "http://127.0.0.1:4200/",//2,
    publicPath:"http://127.0.0.1:8000/static/bundles/",

    headers: {
      'Access-Control-Allow-Origin': '\\*'//3
    }
  }
};
