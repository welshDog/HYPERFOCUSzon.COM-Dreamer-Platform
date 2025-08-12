# 🤝 Contributing to Grafana By Example

Thank you for your interest in contributing! We welcome contributions from monitoring professionals of all backgrounds.

## 🌟 **Code of Conduct**

This project follows the HYPERFOCUS Zone community standards:
- ✅ Be respectful and inclusive
- ✅ Support neurodivergent developers
- ✅ Share monitoring knowledge openly
- ✅ Provide constructive feedback
- ✅ Help create a welcoming environment

## 🚀 **How to Contribute**

### **Types of Contributions**
- 📊 **Dashboard Templates** - Share your best Grafana configurations
- 📚 **Documentation** - Improve guides and examples
- 🐛 **Bug Reports** - Help us identify issues
- 💡 **Feature Requests** - Suggest new capabilities

### **Dashboard Contribution Process**

#### **1. Prepare Your Dashboard**
- Test thoroughly in a production-like environment
- Add clear descriptions and documentation
- Include data source requirements
- Optimize queries for performance

#### **2. Submit Your Contribution**
``bash
# Fork and clone the repository
git clone https://github.com/YOUR-USERNAME/grafana-by-example.git
cd grafana-by-example

# Create a feature branch
git checkout -b feature/my-awesome-dashboard

# Add your dashboard files
mkdir -p dashboards/my-category/
cp my-dashboard.json dashboards/my-category/
echo "# My Dashboard\nDescription and setup instructions" > dashboards/my-category/README.md

# Commit and push
git add .
git commit -m "Add: My Awesome Dashboard for monitoring XYZ"
git push origin feature/my-awesome-dashboard
``

#### **3. Quality Standards**
- [ ] Dashboard JSON is properly formatted
- [ ] Includes README with setup instructions
- [ ] Data source requirements documented
- [ ] Screenshot provided (if possible)
- [ ] Queries are optimized for performance

## 📋 **Dashboard Categories**

Organize contributions in appropriate categories:
- `infrastructure/` - Server and network monitoring
- `applications/` - Application performance monitoring
- `business/` - Business metrics and KPIs
- `devops/` - CI/CD and deployment monitoring
- `cloud/` - Cloud platform specific dashboards
- `databases/` - Database performance monitoring

## 🏆 **Recognition**

Contributors are recognized through:
- Credits in dashboard documentation
- Contributors section in main README
- GitHub contributor statistics
- Community showcase highlighting

## 📞 **Getting Help**

- 💬 **Discussions:** [GitHub Discussions](https://github.com/welshdog/grafana-by-example/discussions)
- 🐛 **Issues:** [GitHub Issues](https://github.com/welshdog/grafana-by-example/issues)

## 🎊 **Thank You!**

Your contributions help the monitoring community build better observability solutions!

---

**Built with 💎 by the HYPERFOCUS Zone community**
