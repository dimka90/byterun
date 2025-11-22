### Design Decisions

1. **Stack Implementation**: Used Python list with validation for 256-bit values and 1024-item limit
2. **Memory Model**: Bytearray with automatic expansion and gas calculation
3. **Storage Model**: Dictionary-based persistent storage
4. **Gas Metering**: Tracked per-operation with dynamic costs for storage
5. **Type Safety**: Pydantic models for all data structures

---

## 📚 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [Opcode Reference](docs/OPCODES.md)
- [Gas Costs](docs/GAS.md)
- [Testing Strategy](docs/TESTING.md)
- [Development Guide](docs/DEVELOPMENT.md)

---

## 🎓 Learning Journey

This project was built to deeply understand Ethereum's execution layer:

1. **Started with**: Basic bytecode interpreter concept
2. **Learned**: EVM specifications, opcodes, gas mechanics
3. **Implemented**: Full EVM with 50+ opcodes
4. **Tested**: 100+ tests covering edge cases and properties
5. **Documented**: Complete architecture and design decisions

### Key Learnings

- **256-bit arithmetic**: Overflow/underflow handling
- **Memory expansion**: Dynamic gas costs
- **Storage patterns**: SLOAD/SSTORE gas mechanics
- **Stack manipulation**: DUP/SWAP operations
- **Testing strategies**: Property-based and fuzz testing

---

## 🛠️ Development

### Setup Development Environment
```bash
make setup
```

### Run Tests
```bash
make test
```

### Build Docker Image
```bash
make build
```

### Run in Docker
```bash
make run
```

---

## 🔮 Future Enhancements

- [ ] Precompiled contracts
- [ ] CALL family opcodes
- [ ] CREATE/CREATE2
- [ ] Real-world bytecode execution
- [ ] EVM trace visualization
- [ ] Comparison with geth/execution-specs

---

## 📖 References

- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf)
- [evm.codes](https://www.evm.codes/)
- [Ethereum Execution Layer Specification (EELS)](https://github.com/ethereum/execution-specs)
- [Ethereum Execution Specification Tests (EEST)](https://github.com/ethereum/execution-spec-tests)

---

## 🤝 Contributing

This is an educational project, but feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch
3. Add tests for any new functionality
4. Ensure all tests pass
5. Submit a pull request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

## 👤 Author

**FILIBUS YILRIT DIMKA**

Built as preparation for Ethereum Foundation internship application.

- GitHub: [@dimka90](https://github.com/dimka90)
- Project: [evm-py](https://github.com/dimka90/byterun)

---

## 🙏 Acknowledgments

- Ethereum Foundation for protocol specifications
- evm.codes for excellent opcode reference
- Python community for amazing testing tools

---

<div align="center">

**If this project helped you understand the EVM, please ⭐ star it!**

</div>
