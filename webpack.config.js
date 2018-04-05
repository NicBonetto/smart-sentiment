var webpack = require('webpack');
var path = require('path');

module.exports = {
  entry: ['babel-polyfill', path.join(__dirname, 'src/')],
  output: {
    path: path.join(__dirname, '/build/'),
    filename: 'app.bundle.js'
  },
  module: {
    rules: [
      {
        exclude: /node_modules/,
        test: /\.js$/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  }
}