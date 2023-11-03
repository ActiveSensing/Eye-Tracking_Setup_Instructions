/// FicTrac http://rjdmoore.net/fictrac/
/// \file       SocketRecorder.cpp
/// \brief      Implementation of socket recorder based on boost::asio UDP datagrams.
/// \author     Richard Moore
/// \copyright  CC BY-NC-SA 3.0

#if 0	// TCP sockets

#ifdef __APPLE__ || __linux__
#include "SocketRecorder_linux.src"
#elif _WIN32
#include "SocketRecorder_win.src"
#endif

#else	// UDP sockets

#include "SocketRecorder.h"

#include "Logger.h"

#include <boost/asio.hpp>

#include <string>

#include <windows.h>

using namespace std;
using boost::asio::ip::udp;

///
///
///
SocketRecorder::SocketRecorder()
    //: _socket(_io_service)
{
    _type = SOCK;
}

///
///
///
SocketRecorder::~SocketRecorder()
{
    closeRecord();
}

///
///
///
bool SocketRecorder::openRecord(std::string host_port)
{
    //// extract host name and port
    //size_t pos = host_port.find_first_of(':');
    //if (pos == string::npos) {
    //    LOG_ERR("Error! Malformed host:port string.");
    //    return false;
    //}
    //_host = host_port.substr(0, pos);
    //_port = stoi(host_port.substr(pos + 1));

    //_endpoint = udp::endpoint(boost::asio::ip::address::from_string(_host), _port);

    //LOG("Opening UDP connection to %s:%d", _host.c_str(), _port);

    //// open socket
    //try {
    //    _socket.open(udp::v4());

    //    _open = _socket.is_open();
    //    if (!_open) { throw; }
    //}
    //catch (const boost::system::system_error& e) {
    //    LOG_ERR("Error! Could not open UDP connection to %s:%d due to %s", _host.c_str(), _port, e.what());
    //    _open = false;
    //}
    //catch (...) {
    //    LOG_ERR("Error! Could not open UDP connection to %s:%d.", _host.c_str(), _port);
    //    _open = false;
    //}

    size_t pos = host_port.find_first_of(':');
    FileMappingName = host_port.substr(pos + 1);
    hMapFile = CreateFileMapping(INVALID_HANDLE_VALUE, NULL, PAGE_READWRITE, 0, 1024, FileMappingName.c_str());
    LOG_ERR("Map with the name " + FileMappingName, GetLastError());

    if (hMapFile != NULL) {
        pBuf = (char*)MapViewOfFile(hMapFile, FILE_MAP_ALL_ACCESS, 0, 0, 1024);
        _open = pBuf != NULL;

        if (!_open) {
            LOG_ERR("MapViewOfFile failed with the name ", FileMappingName, GetLastError());
            CloseHandle(hMapFile);
        }
    }
    else
    {
        LOG_ERR("CreateFileMapping failed with the name ", FileMappingName, GetLastError());
    }

    return _open;
}

///
///
///
bool SocketRecorder::writeRecord(string s)
{
    if (_open) {
        try {
            //_socket.send_to(boost::asio::buffer(s), _endpoint);


            strcpy_s(pBuf, 1024, s.c_str());

        }
        catch (const boost::system::system_error& e) {
            //LOG_ERR("Error writing to socket (%s:%d)! Error was %s", _host.c_str(), _port, e.what());
            LOG_ERR("Error writing to socket: ", FileMappingName);
            return false;
        }
    }
    return _open;
}

///
///
///
void SocketRecorder::closeRecord()
{
    LOG("Closing UDP connection...");

    _open = false;
    //_socket.close();
    UnmapViewOfFile(pBuf);
    CloseHandle(hMapFile);
}
#endif
