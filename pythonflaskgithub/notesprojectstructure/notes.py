from app import app
app.config['SECRET_KEY'] = 'you-will-never-guess'

if __name__ == "__main__":         # Protect this code to be ran if he is imported
    app.run(port=5000, debug=True)



# Example of downloads
# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     # Appending app path to upload folder path within app root folder
#     uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#     # Returning file from appended path
#     return send_from_directory(directory=uploads, filename=filename)