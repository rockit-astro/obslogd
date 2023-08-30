RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} --define "_version $$(date --utc +%Y%m%d%H%M%S)" -ba rockit-obslog.spec
	mv build/noarch/*.rpm .
	rm -rf build

install:
	@cp obslogd /bin/
	@cp obslogd@.service /usr/lib/systemd/system/
	@echo ""
	@echo "Installed server and service files."
