from flask import Flask, render_template, request, jsonify
import os

from chat_app import chat_app as app


@app.route("/data/mirror", methods=['POST'])
def mirror():
    message = request.form['messageText'].encode('utf-8').strip()
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.error('An error occurred')
    ip = request.remote_addr
    print(ip)
    app.logger.info(ip)
    # app.logger.info('Info')
    return jsonify({'status': 'OK', 'answer': message})

