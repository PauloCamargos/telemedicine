# -*- coding: utf-8 -*-UserMixin
import sys
sys.path.append('app');
from app import app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
