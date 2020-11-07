import hashlib
import socket
import ssl

from flask import jsonify


class Fingerprint:

    def __get_certificate(self, url):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        wrapped_socket = ssl.wrap_socket(sock)

        try:
            wrapped_socket.connect((url, 443))

        except:
            return jsonify({"status": 0, "message": "url error"}), 400
        else:
            der_cert_bin = wrapped_socket.getpeercert(True)
            ssl.DER_cert_to_PEM_cert(wrapped_socket.getpeercert(True))
            thumb_md5 = hashlib.md5(der_cert_bin).hexdigest()
            thumb_sha1 = hashlib.sha1(der_cert_bin).hexdigest()
            thumb_sha256 = hashlib.sha256(der_cert_bin).hexdigest()
            wrapped_socket.close()
            return {"md5": thumb_md5, "sha1": thumb_sha1, "sha256": thumb_sha256}

    def get_all(self, url):
        all_fingerprint = self.__get_certificate(url)
        return jsonify({"status": 1, "md5": all_fingerprint["md5"],
                        "sha1": all_fingerprint["sha1"],
                        "sha256": all_fingerprint["sha256"]}), 200

    def get_md5(self, url):
        all_fingerprint = self.__get_certificate(url)
        return jsonify({"status": 1, "md5": all_fingerprint["md5"]}), 200

    def get_sha1(self, url):
        all_fingerprint = self.__get_certificate(url)
        return jsonify({"status": 1, "sha1": all_fingerprint["sha1"]}), 200

    def get_sha256(self, url):
        all_fingerprint = self.__get_certificate(url)
        return jsonify({"status": 1, "sha256": all_fingerprint["sha256"]}), 200
