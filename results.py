from flask import jsonify


class Output:
    def results(data, msg, status_code):
        return (
            jsonify(
                {
                    "author": "Latip176",
                    "data": data,
                    "msg": msg,
                }
            ),
            status_code,
        )
