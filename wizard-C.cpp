#include <io-stream>

using namespace std;

int main()
{
  std::ifstream App("App.py", std::ios::in);
  if (App.is_open()) {
    std::string line;
    while (std::getline(App, line)) {
      std::cout << line << '\n';
    }
    App.close();
  }
  else {
    std::cerr << "Unable to open file\n";
  }
}
