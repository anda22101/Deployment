from flaskapp import app, db, socketio

if __name__ == '__main__':
    if os.getenv('VERCEL'):  
        db_path = '/tmp/site.db' 
        if not os.path.exists(db_path):
            with app.app_context():
                db.create_all()  
    else:
       
        with app.app_context():
            db.create_all()

    # Start the SocketIO server
    socketio.run(app, debug=True)
