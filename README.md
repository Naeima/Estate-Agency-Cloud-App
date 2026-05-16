# Estate Agency Cloud App

A cloud-based estate agency application developed in Python.  
The system simulates a distributed property management platform composed of a server (data warehouse) and clients that browse and interact with property data.

---

##  Overview

This project demonstrates the implementation of a simple cloud application architecture for an estate agency system. The application consists of:

- A **data warehouse/server**
- A **client application**
- A **visitor module** for browsing estate data

The project illustrates basic concepts of:

- Client–server communication
- Cloud application structure
- Distributed systems
- Python network programming

Repository: :contentReference[oaicite:0]{index=0}

---

##  Project Structure

```text
.
├── estate_agency.py    # Main server/data warehouse
├── client.py           # Client application
├── visit.py            # Visitor/browsing module
└── README.md           # Project documentation
```

---

##  Requirements

- Python 3.x

No external libraries are required for the basic implementation.

---

##  Running the Application

### 1. Start the Server

```bash
python estate_agency.py
```

### 2. Run the Client

Open another terminal and execute:

```bash
python client.py
```

### 3. Visitor Access

To browse the estate listings:

```bash
python visit.py
```

---

##  Features

- Cloud-inspired client/server architecture
- Property browsing functionality
- Centralised data warehouse simulation
- Modular Python implementation
- Lightweight and educational design

---

## 📚 Citation

If you use this project in your research or teaching, please cite it as:

```bibtex
@software{hamed2026estatecloud,
  author = {Naeima Hamed},
  title = {Estate Agency Cloud App},
  year = {2019},
  url = {https://github.com/Naeima/Estate-Agency-Cloud-App}
}
```

## License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026 Naeima Hamed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
