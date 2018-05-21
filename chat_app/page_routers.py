from flask import Flask, render_template, request, jsonify
import os

from chat_app import chat_app as app


@app.route("/")
def chat_index():
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    # app.logger.info('Info')
    ip = request.remote_addr
    print(ip)
    app.logger.info(ip)
    return render_template('chat.html')


