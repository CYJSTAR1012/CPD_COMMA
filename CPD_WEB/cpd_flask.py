from flask import Flask, request, jsonify

app = Flask(__name__)

current_emotion = None

@app.route('/trigger', methods=['POST'])
def update_emotion():
    try:
        data = request.get_json(force=True)
        emotion = data.get("emotion")
        # 허용 값도 수정!
        if emotion not in ["SLEEPY", "RELAXED", "STRESSED"]:
            return jsonify({"error": "Invalid emotion type"}), 400
        global current_emotion
        current_emotion = emotion
        print(f"💡 감정 수신됨: {emotion}")
        return jsonify({"status": f"{emotion} received"}), 200
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return jsonify({"error": "Invalid request", "detail": str(e)}), 400

@app.route('/emotion', methods=['GET'])
def get_emotion():
    global current_emotion
    if current_emotion is None:
        return "NONE", 200
    # 값 그대로 반환 (아두이노에서 바로 비교 가능)
    return current_emotion, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
